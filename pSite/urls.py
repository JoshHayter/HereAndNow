from django.conf.urls import url

from . import views

app_name = 'pSite'

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    url(r'^info$', views.info, name='info'),
    url(r'^slideshow$', views.slideshow, name='slideshow'),
    url(r'^success$', views.success, name='success'),
    url(r'^cancel$', views.cancel, name='cancel'),
    url(r'^(?P<item_id>[0-9]+)/charge/$', views.charge, name='charge'),]
