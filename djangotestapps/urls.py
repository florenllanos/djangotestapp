from django.conf.urls import patterns, include, url
from django.contrib import admin
import gesevent.views

# DEPRECATED DJANGO 1.9
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotestapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#   url(r'^gesevent/tematica/crear/$', 'gesevent.views.tematica_crear',
#       name='tematica_crear'),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gesevent/tematica/crear/$', gesevent.views.tematica_crear,
        name='tematica_crear'),
]
