from wtforms.fields.core import SelectField
from wtforms.fields.simple import SubmitField
from wtforms.form import Form

__author__ = 'e83800'

class UpdateAirportForm(Form):
    airport = SelectField(u'Airport to update')
    submit = SubmitField()