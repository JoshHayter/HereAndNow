from django.conf.urls import url

from . import views

app_name = 'pSite'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^slideshow$', views.slideshow, name='slideshow'),
    url(r'^success$', views.success, name='success'),
    url(r'^cancel$', views.cancel, name='cancel'),
    url(r'^(?P<item_id>[0-9]+)/charge/$', views.charge, name='charge'),]
