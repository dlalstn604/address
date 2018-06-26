from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.address_list, name='address_list'),
    url(r'^address/(?P<pk>\d+)/$', views.address_detail, name='address_detail'),
    url(r'^address/new/$', views.address_new, name='address_new'),
    url(r'^address/(?P<pk>\d+)/address/$', views.address_edit, name='address_edit'),
]