from wtforms.widgets.core import TextInput
from local_settings import MAX_HOPS

__author__ = 'e83800'

class CalendarInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs['data-role'] = "datebox"
        kwargs['data-options'] = '{"mode":"calbox","afterToday": true, "useInline": true, "hideInput": true}'
        return super(CalendarInput, self).__call__(field, **kwargs)

class SliderInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs['type'] = "range"
        kwargs['value'] = "2"
        kwargs['min'] = "1"
        kwargs['max'] = str(MAX_HOPS)
        return super(SliderInput, self).__call__(field, **kwargs)
