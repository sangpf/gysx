from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.detail),

    url(r'^user/add_user_page/$',views.add_user_page),
    url(r'^user/add_user/$',views.add_user),
    url(r'^user/get_userList/$',views.get_userList),
    url(r'^user/(?P<id>\d+)/$',views.get_user_id),
    url(r'^user/delete/(?P<id>\d+)/$',views.delete_user_id),
    url(r'^user/update/(?P<id>\d+)/$',views.update_user),

    url(r'^$',views.index, name = 'index'),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$',views.detail, name = 'detail'),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),

    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$',views.postTest2),

]

