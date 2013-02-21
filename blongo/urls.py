from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blogapp.views.index'),
    url(r'^update/', 'blogapp.views.update'),
    url(r'^delete/', 'blogapp.views.delete'),
)
