from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.template.response import TemplateResponse
from social_auth import __version__ as version

__author__ = 'wiper'

def index(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return TemplateResponse(request, 'login/login_index.html', {'version': version}, RequestContext(request))
