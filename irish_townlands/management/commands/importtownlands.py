"""
Management command to conver the OSM imported data in your postgis database to
the django models.
"""
from __future__ import division

from optparse import make_option

from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings
from django.db.models import Sum
from ...models import County, Townland, Barony, CivilParish, TownlandTouch, Metadata, Error, Progress

from collections import defaultdict
import psycopg2
from contextlib import contextmanager
import datetime

DEBUG = False

@contextmanager
def printer(msg):
    """Context statement to print when a task starts & ends."""
    if DEBUG:
        print "Starting "+msg
    yield
    if DEBUG:
        print "Finished "+msg


def err_msg(msg, *args, **kwargs):
    """Log an error message to DB & print it. """
    msg = msg.format(*args, **kwargs)
    Error.objects.create(message=msg)
    print msg


def create_area_obj(name, where_clause, django_model, cols, cursor):
    """Create one type of area."""
    results = {}

    with printer("getting " + name):
        cursor.execute("select {0} from valid_polygon where {1} ;".format(", ".join(c[0] for c in cols), where_clause))

        for row in cursor:
            kwargs = dict(zip([c[1] for c in cols], row))
            new_obj = django_model(**kwargs)
            new_obj.save()

        results = dict((x.osm_id, x) for x in django_model.objects.all().defer("polygon_geojson"))

    return results


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--verbose',
            action='store_true',
            dest='verbose',
            default=False,
            help='Be verbose, and print debugging output'),
        )

    def handle(self, *args, **options):

        if options['verbose']:
            global DEBUG
            DEBUG = True

        # delete old
        with transaction.commit_on_success():
            for obj in [Townland, County, CivilParish, Barony]:
                obj.objects.all().delete()

            # Clear errors
            Error.objects.all().delete()


            cols = [
                ('name', 'name'),
                ('"name:ga"', 'name_ga'),
                ('alt_name', 'alt_name'),
                ('osm_id', 'osm_id'),
                ('st_area(geo)', 'area_m2'),
                ('ST_X(st_transform((ST_centroid(way)), 4326))', 'centre_x'),
                ('ST_Y(st_transform((ST_centroid(way)), 4326))', 'centre_y'),
                ('ST_AsGeoJSON(geo)', 'polygon_geojson'),

            ]

            if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
                # Development testing with sqlite
                conn = psycopg2.connect("dbname='gis'")
            else:
                # using postgres (we presume)
                dbuser, dbpass = settings.DATABASES['default']['USER'], settings.DATABASES['default']['PASSWORD']
                conn = psycopg2.connect(host='127.0.0.1', database="gis", user=dbuser, password=dbpass)

            cursor = conn.cursor()

            townlands = create_area_obj('townlands', "admin_level = '10'", Townland, cols, cursor)

            # touching
            touching_townlands = []
            with printer("touching townlands"):
                cursor.execute("select a.osm_id, b.osm_id, ST_length(st_intersection(a.geo, b.geo)), ST_Azimuth(st_centroid(a.way), st_centroid(st_intersection(a.way, b.way))) from valid_polygon as a inner join valid_polygon as b on st_touches(a.way, b.way) where a.admin_level = '10' and b.admin_level = '10' and a.osm_id <> b.osm_id;")
                for a_osm_id, b_osm_id, length_m, direction_radians in cursor:
                    touching_townlands.append(TownlandTouch(townland_a=townlands[a_osm_id], townland_b=townlands[b_osm_id], length_m=length_m, direction_radians=direction_radians))
                    #townlands[a_osm_id].touching_townlands.add(townlands[b_osm_id])
                    #townlands[b_osm_id].touching_townlands.add(townlands[a_osm_id])
                TownlandTouch.objects.bulk_create(touching_townlands)

            # check if a is touching b, that b is also touching a
            #assert all(all(t in x.touching for x in t.touching) for t in townlands.values())


            # manually create counties
            with printer("creating counties"):

                county_names = set([
                    "Tyrone", "Kerry", "Dublin", "Down", "Fermanagh", "Wexford", "Mayo", "Carlow",
                    "Wicklow", "Longford", "Westmeath", "Cork", "Leitrim", "Laois", "Waterford", "Tipperary",
                    "Monaghan", "Kilkenny", "Galway", "Meath", "Donegal", "Cavan", "Kildare", "Offaly",
                    "Derry", "Clare", "Armagh", "Antrim", "Limerick", "Louth", "Sligo", "Roscommon",
                    ])
                counties = create_area_obj('counties', "admin_level = '6'", County, cols, cursor)
                for c in counties.values():
                    original_county_name = c.name

                    # sanitize name
                    if c.name.startswith("County "):
                        c.name = c.name[7:]
                    if c.name == 'Londonderry':
                        c.name = u'Derry'

                    # calculate amount of water in this county
                    cursor.execute("""
                        select sum(
                           case
                             when st_within(water_polygon.way, valid_polygon.way) then ST_Area(water_polygon.geo)
                             else ST_Area(ST_Intersection(valid_polygon.geo, water_polygon.geo))
                           end) as water_area_m2
                        from valid_polygon inner join water_polygon ON ST_Intersects(valid_polygon.way, water_polygon.way)
                        where valid_polygon.admin_level  = '6' and name = '{original_county_name}'
                    """.format(original_county_name=original_county_name))
                    water_area_m2 = list(cursor)
                    assert len(water_area_m2) == 1
                    water_area_m2 = water_area_m2[0][0] or 0
                    c.water_area_m2 = water_area_m2
                    if c.water_area_m2 >= c.area_m2:
                        err_msg("County {0}, too much water?", c.name)

                    c.save()

                    if not any(c.is_name(county_name) for county_name in county_names):
                        print "Deleting dud county ", c.name
                        del counties[c.osm_id]
                        c.delete()
                    else:
                        c.generate_url_path()
                        c.save()

                seen_counties = set([c.name for c in counties.values()])
                missing_counties = county_names - seen_counties
                for missing in missing_counties:
                    err_msg("Could not find County {0}. Is the county boundary/relation broken?", missing)


            baronies = create_area_obj('baronies', "boundary = 'barony'", Barony, cols, cursor)
            civil_parishes = create_area_obj('civil parishes', "boundary = 'civil_parish'", CivilParish, cols, cursor)

            # remove "Civil Parish" suffix from C.P.s
            for cp in civil_parishes.values():
                if cp.name.lower().endswith(" civil parish"):
                    cp.name = cp.name[:-len(" civil parish")]

            # remove "Barony of" suffix from baronies
            for b in baronies.values():
                if b.name.lower().startswith("barony of "):
                    cp.name = cp.name[len("barony of "):]


            # townland in county


            with printer("townlands in counties"):
                cursor.execute("select c.name, t.osm_id from valid_polygon as c join valid_polygon as t on (c.admin_level = '6' and t.admin_level = '10' and st_contains(c.way, t.way));")

                for county_name, townland_osm_id in cursor:
                    county = [c for c in counties.values() if c.is_name(county_name)]

                    if len(county) == 0:
                        err_msg("Unknown county {0}", county_name)
                    else:
                        if len(county) > 1:
                            err_msg("Townland (OSM ID: {townland_osm_id}) is in >1 counties! Overlapping border? Counties: {counties}", townland_osm_id=townland_osm_id, counties=", ".join(county))
                            break
                        county = county[0]
                        if townland_osm_id not in townlands:
                            err_msg("Weird townland ids")
                            break
                        townland = townlands[townland_osm_id]
                        if townland.county not in [None, county]:
                            err_msg("Townland {townland} is in 2 counties! Overlapping border? First county: {townland.county}, Second county: {county}", townland=townland, county=county)
                        else:
                            townland.county = county


                townlands_not_in_counties = set(t for t in townlands.values() if not hasattr(t, 'county'))
                #assert len(townlands_not_in_counties) == 0, townlands_not_in_counties


            # townland in barony

            with printer("townlands in baronies"):
                cursor.execute("select b.osm_id, t.osm_id from valid_polygon as b join valid_polygon as t on (b.boundary = 'barony' and t.admin_level = '10' and st_contains(b.way, t.way));")

                for barony_osm_id, townland_osm_id in cursor:
                    if not ( townlands[townland_osm_id].barony is None or townlands[townland_osm_id].barony.osm_id == barony_osm_id ):
                        err_msg("Overlapping Baronies")
                    else:
                        townlands[townland_osm_id].barony = baronies[barony_osm_id]
                        townlands[townland_osm_id].save()

            # townland in civil parish
            with printer("townlands in civil parishes"):
                cursor.execute("select b.osm_id, t.osm_id from valid_polygon as b join valid_polygon as t on (b.boundary = 'civil_parish' and t.admin_level = '10' and st_contains(b.way, t.way));")

                for cp_osm_id, townland_osm_id in cursor:
                    townland = townlands[townland_osm_id]
                    other_cp = civil_parishes[cp_osm_id]
                    if not ( townland.civil_parish is None or townland.civil_parish.osm_id == cp_osm_id ):
                        err_msg("County {county}, Townland {td} is in civil parish {cp1} and {cp2}. Overlapping Civil Parishes?", td=townland, cp1=townland.civil_parish, cp2=other_cp, county=townland.county)
                    else:
                        townlands[townland_osm_id].civil_parish = civil_parishes[cp_osm_id]
                        townlands[townland_osm_id].save()


            for barony in baronies.values():
                barony.calculate_county()
            for civil_parish in civil_parishes.values():
                if civil_parish.townlands.count() == 0:
                    err_msg("No townlands in Civil Parish {0}".format(civil_parish.name))
                else:
                    civil_parish.calculate_county()

            def _calculate_gaps_and_overlaps(osm_id, sub_ids):
                # gap
                sql = """select st_AsGeoJSON(
                                st_geographyfromtext(st_astext(st_transform(
                                st_difference(county.way, all_townlands.way)
                                , 4326))))
                        from (select way from valid_polygon where osm_id = {osm_id}) as county, (select st_union(way) as way from valid_polygon where osm_id in ({sub_osm_ids}) ) as all_townlands;""".format(osm_id=osm_id, sub_osm_ids=",".join(sub_ids))
                cursor.execute(sql)
                details = list(cursor)
                assert len(details) == 1
                gaps = details[0][0] or ""
                if gaps == '{"type":"GeometryCollection","geometries":[]}':
                    # Simplify
                    gaps = ""

                # overlap
                sql = """select
                            st_AsGeoJSON(st_geographyfromtext(st_astext(st_transform(
                                st_union(st_intersection(st_difference(a.way, st_boundary(a.way)), st_difference(b.way, st_boundary(b.way))))
                            , 4326))))
                    from (select osm_id, way from valid_polygon where osm_id in ({sub_osm_ids})) as a, (select osm_id, way from valid_polygon where osm_id in ({sub_osm_ids})) as b where a.osm_id <> b.osm_id and st_overlaps(a.way, b.way);""".format(sub_osm_ids=",".join(sub_ids))
                cursor.execute(sql)
                details = list(cursor)
                assert len(details) == 1
                overlaps = details[0][0] or ''

                return gaps, overlaps

            # County level gaps in coverage of townlands
            with printer("finding land in county not covered by townlands"):
                for county in counties.values():

                    # townlands

                    these_townlands = set(str(t.osm_id) for t in townlands.values() if t.county == county)
                    if len(these_townlands) == 0:
                        # Shortcut, there are no townlands here
                        county.polygon_townland_gaps = county.polygon_geojson
                        county.polygon_townland_overlaps = ''
                    else:
                        county.polygon_townland_gaps, county.polygon_townland_overlaps = _calculate_gaps_and_overlaps(county.osm_id, these_townlands)

                    # baronies

                    these_baronies = set(str(b.osm_id) for b in baronies.values() if b.county == county)
                    if len(these_baronies) == 0:
                        # Shortcut, there are no baronies here
                        county.polygon_barony_gaps = county.polygon_geojson
                        county.polygon_barony_overlaps = ''
                    else:
                        county.polygon_barony_gaps, county.polygon_barony_overlaps = _calculate_gaps_and_overlaps(county.osm_id, these_baronies)

                    # civil parishes
                    these_civil_parishes = set(str(cp.osm_id) for cp in civil_parishes.values() if cp.county == county)
                    if len(these_civil_parishes) == 0:
                        # Shortcut, there are no civil_parishes here
                        county.polygon_civil_parish_gaps = county.polygon_geojson
                        county.polygon_civil_parish_overlaps = ''
                    else:
                        county.polygon_civil_parish_gaps, county.polygon_civil_parish_overlaps = _calculate_gaps_and_overlaps(county.osm_id, these_civil_parishes)

                    county.save()



            with printer("uniqifying townland urls"):
                all_areas = set(townlands.values()) | set(civil_parishes.values()) | set(baronies.values()) | set(counties.values())
                for x in all_areas:
                    x.generate_url_path()


                overlapping_url_paths = defaultdict(set)
                for x in all_areas:
                    overlapping_url_paths[x.url_path].add(x)
                for url_path in overlapping_url_paths:
                    if len(overlapping_url_paths[url_path]) == 1:
                        continue
                    for x, i in zip(sorted(overlapping_url_paths[url_path], key=lambda x: x.area_m2), range(1, len(overlapping_url_paths[url_path])+1)):
                        x.unique_suffix = i
                        x.save()
                        x.generate_url_path()

                assert len(set(t.url_path for t in townlands.values())) == len(townlands)

            # save all now
            with printer("final objects save"):
                for objs in [townlands, civil_parishes, baronies, counties]:
                    for x in objs.values():
                        x.save()

            with printer("recording progress"):
                area_of_ireland = County.objects.all().aggregate(Sum('area_m2'))['area_m2__sum'] or 0
                area_of_all_townlands = Townland.objects.all().aggregate(Sum('area_m2'))['area_m2__sum'] or 0
                if area_of_ireland == 0:
                    townland_progress = 0
                else:
                    townland_progress = ( area_of_all_townlands / area_of_ireland ) * 100
                Progress.objects.create(percent=townland_progress, name="ireland-tds")
                for county in County.objects.all():
                    Progress.objects.create(percent=county.townland_cover, name=county.name+"-tds")

            with printer("updating metadata"):
                last_updated, _ = Metadata.objects.get_or_create(key="lastupdate")
                last_updated.value = datetime.datetime.utcnow().isoformat()
                last_updated.save()

