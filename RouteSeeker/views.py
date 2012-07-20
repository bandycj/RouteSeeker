from django.template.response import TemplateResponse

__author__ = 'wiper'

def index(request):
    return TemplateResponse(request, 'index.html')