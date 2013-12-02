from django.conf.urls import patterns, include, url
from .views import BoatList, BoatCreate, BoatDetail, BoatUpdate, BoatDelete

urlpatterns = patterns('',
    # Boat
    url(r'^boat/all/$', BoatList.as_view(), name='boat_list'),
    url(r'^boat/add$', BoatCreate.as_view(), name='boat_add'),
    url(r'^boat/detail/(?P<pk>\d+)/$', BoatDetail.as_view(), name='boat_detail'),
    url(r'^boat/update/(?P<pk>\d+)/$', BoatUpdate.as_view(), name='boat_update'),
    url(r'^boat/delete/(?P<pk>\d+)/$', BoatDelete.as_view(), name='boat_delete'),
)
