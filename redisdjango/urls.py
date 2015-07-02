from django.conf.urls import patterns, include, url
from apps.api.urls import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^api/' , include(v1_api.urls)), 
	(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
    # Examples:
    # url(r'^$', 'redisdjango.views.home', name='home'),
    # url(r'^redisdjango/', include('redisdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += patterns('',
			url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 
				'document_root': settings.MEDIA_ROOT,
				 }), 
			)
