from django.conf.urls import patterns, url
#from django.conf.urls import include
#from .views import index, index2

urlpatterns = patterns('',
	#url(r'^$', 'apps.inicio.views.index'),
	#url(r'^$', index.as_view()),

	url(r'^$', 'django.contrib.auth.views.login',
		{'template_name':'inicio/index.html'}, name = 'login'),

	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',
		name = 'logout'),
)