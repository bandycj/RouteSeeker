from django.template.response import TemplateResponse
from apps.search.forms import SearchForm
from apps.search.models import Airport, Flight

def index(request):
    form = SearchForm()
    choices = []
    for airport in Airport.objects.all().order_by('iataCode'):
        choices.append((airport.iataCode, airport.name))

    form.origin.choices = choices
    form.destination.choices = choices

    return TemplateResponse(request, 'search/search_index.html', {'form': form})


def result(request, origin=None, destination=None):
    if request.method == 'POST':
        o = Airport.objects.get(pk=origin)
        d = Airport.objects.get(pk=destination)
        flights = Flight.objects.filter(origin=o, destination=d)

        return TemplateResponse(request, 'search/search_result.html', {
            'flights': flights
        })
