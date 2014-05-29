#! /bin/bash

set -o errexit

BASEDIR=$(dirname $0)
cd ${BASEDIR}

# In case these are still around
for TABLE in valid_polygon water_polygon planet_osm_nodes planet_osm_rels planet_osm_ways planet_osm_line planet_osm_line planet_osm_point planet_osm_roads planet_osm_polygon planet_osm_roads_tmp; do
	PGOPTIONS="--client-min-messages=warning" psql -q -d gis -c "drop table if exists $TABLE;"
done


wget -q -N http://download.geofabrik.de/openstreetmap/europe/ireland-and-northern-ireland.osm.pbf
osm2pgsql --cache 50M --slim --style ./osm2pgsql.style -G ireland-and-northern-ireland.osm.pbf
rm ireland-and-northern-ireland.osm.pbf

# not needed anymore
for TABLE in planet_osm_nodes planet_osm_rels planet_osm_ways planet_osm_line planet_osm_line planet_osm_point planet_osm_roads; do
	PGOPTIONS="--client-min-messages=warning" psql -q -d gis -c "drop table if exists $TABLE;"
done

psql -q -d gis -c "create table valid_polygon as select * from planet_osm_polygon where name IS NOT NULL and st_isvalid(way) and (admin_level is not null or boundary is not null)";
psql -q -d gis -c "create table water_polygon as select way from planet_osm_polygon where water IS NOT NULL OR waterway IS NOT NULL OR \"natural\" = 'water' and st_isvalid(way)";

psql -q -d gis -c "drop table planet_osm_polygon;"


psql -q -d gis -c "create index valid_polygon__way on valid_polygon using GIST (way); create index valid_polygon__admin_level on valid_polygon (admin_level); create index valid_polygon__name on valid_polygon (name);"
psql -q -d gis -c "create index water_polygon__way on water_polygon using GIST (way);"

psql -q -d gis -c "alter table valid_polygon add column geo geography;"
psql -q -d gis -c "update valid_polygon set geo = st_geographyfromtext(astext(transform(way, 4326)));"

psql -q -d gis -c "alter table water_polygon add column geo geography;"
psql -q -d gis -c "update valid_polygon set geo = st_geographyfromtext(astext(transform(way, 4326)));"

cd ${BASEDIR}
#./screenshot-townlands.sh
