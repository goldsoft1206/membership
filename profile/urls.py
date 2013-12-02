from django.conf.urls import patterns, include, url
from .views import BoatList, BoatCreate, BoatDetail, BoatUpdate, BoatDelete,\
                   MembershipTypeList, MembershipTypeCreate, MembershipTypeDetail, MembershipTypeUpdate, MembershipTypeDelete

urlpatterns = patterns('',
    # Boat
    url(r'^boat/all/$', BoatList.as_view(), name='boat_list'),
    url(r'^boat/add/$', BoatCreate.as_view(), name='boat_add'),
    url(r'^boat/detail/(?P<pk>\d+)/$', BoatDetail.as_view(), name='boat_detail'),
    url(r'^boat/update/(?P<pk>\d+)/$', BoatUpdate.as_view(), name='boat_update'),
    url(r'^boat/delete/(?P<pk>\d+)/$', BoatDelete.as_view(), name='boat_delete'),

    # MembershipType
    url(r'^mtype/all/$', MembershipTypeList.as_view(), name='mtype_list'),
    url(r'^mtype/add/$', MembershipTypeCreate.as_view(), name='mtype_add'),
    url(r'^mtype/detail/(?P<pk>\d+)/$', MembershipTypeDetail.as_view(), name='mtype_detail'),
    url(r'^mtype/update/(?P<pk>\d+)/$', MembershipTypeUpdate.as_view(), name='mtype_update'),
    url(r'^mtype/delete/(?P<pk>\d+)/$', MembershipTypeDelete.as_view(), name='mtype_delete'),
)
