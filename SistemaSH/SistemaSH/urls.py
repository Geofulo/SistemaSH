from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaSH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^' , include('apps.inicio.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    	{'document_root': settings.MEDIA_ROOT,}),
    url(r'^modelos/', include('apps.modelos.urls')),
    url(r'^colores/', include('apps.colores.urls')),    
)
