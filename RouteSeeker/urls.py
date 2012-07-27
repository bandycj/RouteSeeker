from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http import HttpResponse
from apps.login.views import done

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^$', 'RouteSeeker.views.index', name='home'),
    url(r'^done/$', done, name='done'),
#    url(r'^error/$', error, name='error'),
#    url(r'^logout/$', logout, name='logout'),
    url(r'^search/$', 'apps.search.views.index'),
    url(r'^schedule/$', 'apps.schedule.views.index'),
    url(r'^schedule/update_airports$', 'apps.schedule.views.update_airports'),
    url(r'^schedule/update_timezones$', 'apps.schedule.views.update_timezones'),
    url(r'^schedule/update_schedule', 'apps.schedule.views.update_schedule'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),
)
