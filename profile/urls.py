from django.conf.urls import patterns, include, url
from .views import BoatList, BoatCreate, BoatDetail, BoatUpdate, BoatDelete,\
                   MembershipTypeList, MembershipTypeCreate, MembershipTypeDetail, MembershipTypeUpdate, MembershipTypeDelete,\
                   MembershipList, MembershipCreate, MembershipDetail, MembershipUpdate, MembershipDelete,\
                   EmailListView, EmailCreate, EmailDetail, EmailUpdate, EmailDelete

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

    # Membership
    url(r'^membership/all/$', MembershipList.as_view(), name='membership_list'),
    url(r'^membership/add/$', MembershipCreate.as_view(), name='membership_add'),
    url(r'^membership/detail/(?P<pk>\d+)/$', MembershipDetail.as_view(), name='membership_detail'),
    url(r'^membership/update/(?P<pk>\d+)/$', MembershipUpdate.as_view(), name='membership_update'),
    url(r'^membership/delete/(?P<pk>\d+)/$', MembershipDelete.as_view(), name='membership_delete'),

    # EmailList
    url(r'^emaillist/all/$', EmailListView.as_view(), name='email_list'),
    url(r'^emaillist/add/$', EmailCreate.as_view(), name='email_add'),
    url(r'^emaillist/detail/(?P<pk>\d+)/$', EmailDetail.as_view(), name='email_detail'),
    url(r'^emaillist/update/(?P<pk>\d+)/$', EmailUpdate.as_view(), name='email_update'),
    url(r'^emaillist/delete/(?P<pk>\d+)/$', EmailDelete.as_view(), name='email_delete'),
)
