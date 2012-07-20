from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.datetime_safe import datetime
from apps.schedule.forms import UpdateAirportForm
from apps.search.models import Airport, Flight
from utils.location_utils import get_airports, get_timezones
from utils.schedule_utils import get_schedule

def index(request):
    return TemplateResponse(request, 'schedule/schedule_index.html')


def update_airports(request):
    airports = get_airports()
    for airport in airports:
        Airport.objects.get_or_create(**airport)

    return TemplateResponse(request, 'schedule/schedule_update_airports.html', {
        'airports': Airport.objects.all()
    })


def update_timezones(request):
    timezones = get_timezones()
    return TemplateResponse(request, 'schedule/schedule_update_timezones.html', {
        'timezones': timezones
    })

def update_schedule(request, iataCode=None):
    form = UpdateAirportForm(request.POST)
    choices = []
    for airport in Airport.objects.all().order_by('iataCode'):
        choices.append((airport.iataCode, airport.name))

    form.airport.choices = choices
    if request.method == 'POST' and form.validate():
        flights = get_schedule(form.airport.data)
        
        for flight in flights:
            new_flight = {
                'origin': Airport.objects.get(pk=flight['origin']),
                'destination': Airport.objects.get(pk=flight['destination']),
                'flightNum': flight['flightNum'],
                'fromDate': datetime.strptime(flight['fromDate'], "%B %d, %Y"),
                'toDate': datetime.strptime(flight['toDate'], "%B %d, %Y"),
                'skd': datetime.strptime(flight['ska'], "%I:%M%p"),
                'ska': datetime.strptime(flight['skd'], "%I:%M%p")
            }
            Flight.objects.get_or_create(**new_flight)
        return redirect('/schedule')
    else:

        return TemplateResponse(request, 'schedule/schedule_update_schedule.html', {
            'form': form,
            })
