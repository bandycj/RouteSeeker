from wtforms.fields.core import SelectField
from wtforms.fields.simple import TextField
from wtforms.fields.core import IntegerField
from wtforms.form import Form
from utils.widgets import SliderInput, CalendarInput

__author__ = 'e83800'

class SearchForm(Form):
    origin = SelectField(u'Origin')
    destination = SelectField(u'Destination')
    hops = IntegerField(u'Hops', widget=SliderInput())
    date = TextField(u'Date', widget=CalendarInput())