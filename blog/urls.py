from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.address_list, name='address_list'),
    url(r'^address/(?P<pk>\d+)/$', views.address_detail, name='address_detail'),
    url(r'^address/new/$', views.address_new, name='address_new'),
    url(r'^address/(?P<pk>\d+)/address/$', views.address_edit, name='address_edit'),
    url(r'^draft/$', views.address_draft_list, name='address_draft_list'),
    url(r'^address/(?P<pk>\d+)/publish/$', views.address_publish, name='address_publish'),
    url(r'^address/(?P<pk>\d+)/remove/$', views.address_remove, name='address_remove'),
]