"""Views."""
from __future__ import division
import re
from datetime import timedelta, datetime
import math

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Sum, Count

from .models import Metadata, Townland, CivilParish, Barony, County, Error, Progress

COUNTIES = [u'Antrim', u'Armagh', u'Carlow', u'Cavan', u'Clare', u'Cork',
            u'Derry', u'Donegal', u'Down', u'Dublin', u'Fermanagh', u'Galway',
            u'Kerry', u'Kildare', u'Kilkenny', u'Laois', u'Leitrim',
            u'Limerick', u'Longford', u'Louth', u'Mayo', u'Meath', u'Monaghan',
            u'Offaly', u'Roscommon', u'Sligo', u'Tipperary', u'Tyrone',
            u'Waterford', u'Westmeath', u'Wexford', u'Wicklow']



def progress(request):
    try:
        last_update = Metadata.objects.get(key="lastupdate").value
    except Metadata.DoesNotExist:
        last_update = "N/A"
    counties = County.objects.order_by('name').all()
    errors = Error.objects.all().values_list('message', flat=True)

    area_of_ireland_incl_water = County.objects.all().aggregate(Sum('area_m2'))['area_m2__sum'] or 0
    water_of_ireland = County.objects.all().aggregate(Sum('water_area_m2'))['water_area_m2__sum'] or 0
    area_of_ireland_excl_water = area_of_ireland_incl_water - water_of_ireland
    area_of_ireland = area_of_ireland_excl_water

    area_of_all_townlands = Townland.objects.all().aggregate(Sum('area_m2'))['area_m2__sum'] or 0
    area_of_all_civil_parishes = CivilParish.objects.all().aggregate(Sum('area_m2'))['area_m2__sum'] or 0
    area_of_all_baronies = Barony.objects.all().aggregate(Sum('area_m2'))['area_m2__sum'] or 0

    if area_of_ireland == 0:
        townland_progress = civil_parish_progress = barony_progress = 0
    else:
        townland_progress = ( area_of_all_townlands / area_of_ireland ) * 100
        civil_parish_progress = ( area_of_all_civil_parishes / area_of_ireland ) * 100
        barony_progress = ( area_of_all_baronies / area_of_ireland ) * 100

    return render_to_response('irish_townlands/progress.html',
        {
            'counties':counties, 'last_update':last_update, 'errors':errors,
            'townland_progress': townland_progress, 'civil_parish_progress': civil_parish_progress,
            'barony_progress': barony_progress,
         },
        context_instance=RequestContext(request))


def duplicatenames(request):
    # Dupe names. Nothing wrong with duplicate names, it happens
    duplicate_townland_names = []
    duplicate_names = Townland.objects.all().values("name").annotate(count=Count('name')).filter(count__gte=2).order_by('-count', 'name')
    for item in duplicate_names:
        townland_name, townland_count = item['name'], item['count']
        townlands = Townland.objects.filter(name=townland_name).order_by("county__name", "barony__name", "civil_parish__name").values('url_path', 'county__name', 'barony__name', 'civil_parish__name')
        duplicate_townland_names.append({'name': townland_name, 'count': townland_count, 'townlands': townlands})

    return render_to_response('irish_townlands/duplicatenames.html',
        {
            'duplicate_townland_names': duplicate_townland_names,
         },
        context_instance=RequestContext(request))

def county_debug(request, url_path):
    try:
        last_update = Metadata.objects.get(key="lastupdate").value
    except Metadata.DoesNotExist:
        last_update = "N/A"

    # County debug page
    try:
        # strip debug from url to get county
        url_path = re.sub('debug/$', '', url_path)
        x = County.objects.select_related().get(url_path=url_path)
        return render_to_response('irish_townlands/countydebug_detail.html', {'county': x, 'last_update': last_update}, context_instance=RequestContext(request))
    except:
        # Couldn't find county
        raise Http404("County not found")

def view_area(request, url_path=None):
    try:
        last_update = Metadata.objects.get(key="lastupdate").value
    except Metadata.DoesNotExist:
        last_update = "N/A"

    # County index page
    if url_path in ['all', None]:
        return render_to_response('irish_townlands/index.html', {
            'counties': County.objects.only('name', 'url_path').order_by('name').all(),
            'last_update': last_update,
            }, context_instance=RequestContext(request))

    # Detail pages
    for model, name in ( (Townland, 'townland'), (CivilParish, 'civil_parish'), (Barony, 'barony'), (County, 'county')):
        try:
            x = model.objects.select_related().get(url_path=url_path)
            return render_to_response('irish_townlands/'+name+'_detail.html', {name: x, 'last_update': last_update}, context_instance=RequestContext(request))
        except model.DoesNotExist:
            continue  #  on to next model

    # nothing by here?
    raise Http404()

def days_to_string(days):
    days = int(days)
    years, days = divmod(days, 365)
    months, days = divmod(days, 30)
    weeks, days = divmod(days, 7)
    output = ""
    if years > 0:
        output += "%d years" % years
    if months > 0:
        output += " %d months" % months
    if weeks > 0:
        output += " %d weeks" % weeks
    if days > 0:
        output += " %d days" % days

    return output


def format_float(x):
    """
    Return a nice human readable version of a float.

    It will never return something that looks like zero for a non-zero number.

    """

    if x == 0:
        # It's zero, so return
        return "0"
    else:
        # How many decimal places should be show?
        # If x = 0.0002, then if we show to 2 decimal places it'll show 0.00,
        # which looks like zero.
        for exp in range(2, 6):
            if x > math.pow(10, -exp):
                return "{0:.{1}f}".format(x, exp)
            else:
                continue
        else:
            # Haven't found anything, so return a <tinynumber
            return "<{0:.{1}f}".format(math.pow(10, -exp), exp)

def calculate_rate(initial_date, initial_percent, current_date, current_percent, amount_left):
    days = (current_date - initial_date).days
    delta_percent = (current_percent - initial_percent)
    rate = delta_percent / days
    if rate == 0:
        days_left = None
        end_date = None
        human_readable_time_left = None
    else:
        days_left =  int(amount_left / rate)

        try:
            end_date = current_date + timedelta(days=days_left)
        except OverflowError:
            # timedelta gives OverflowError if the days is too far in the future,
            # so cap it, based on datetime.MAXYEAR (which is 9999)
            end_date = "the year {0:.0f}".format(datetime.today().year + (days_left/365))
        human_readable_time_left = days_to_string(days_left)


    return {
        'rate': format_float(rate), 'days_left':days_left, 'end_date':end_date,
        'initial_date': initial_date,
        'human_readable_time_left': human_readable_time_left,
    }


def many_range_rates(name):
    query_set = Progress.objects.filter(name=name+'-tds')
    most_recent_date, most_recent_percent = query_set.order_by("-when", "-id").values_list('when', 'percent')[0]
    amount_left = round(100 - most_recent_percent, 4)
    ## since start
    initial_date, initial_percent = query_set.order_by("when", "-id").values_list('when', 'percent')[0]
    ## since day before
    yesterday_percent = query_set.filter(when=(most_recent_date - timedelta(days=1))).order_by("-id").values_list('percent', flat=True)[0]

    # since last week
    week_percent = query_set.filter(when=(most_recent_date - timedelta(days=7))).values_list('percent', flat=True)
    week_percent = week_percent[0] if len(week_percent) > 0 else None

    return {
        'amount_left': amount_left,
        'since_start': calculate_rate(initial_date, initial_percent, most_recent_date, most_recent_percent, amount_left),
        'since_yesterday': calculate_rate((most_recent_date - timedelta(days=1)), yesterday_percent, most_recent_date, most_recent_percent, amount_left),
        'since_last_week': calculate_rate((most_recent_date - timedelta(days=7)), week_percent, most_recent_date, most_recent_percent, amount_left),
    }


def rate(request):
    results = {}
    results['ireland'] = many_range_rates('ireland')
    results['counties'] = []
    for county in sorted(COUNTIES):
        results['counties'].append((county, many_range_rates(county)))


    return render_to_response('irish_townlands/rate.html', results,
        context_instance=RequestContext(request))
