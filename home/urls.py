from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('login/', views.login_controller.index, name='index'),
    path('loginpost/', views.login_controller.loginpost, name='loginpost'),
    path('speedometer/', views.login_controller.speedometer, name='speedometer'),
    path('app/', views.login_controller.app, name='app'),
    path('test_show/', views.login_controller.test_show, name='test_show'),
    url(r'^loginpost/add_test_entry/(?P<pk>[0-9,a-z,A-Z,.,;,_]+)/$', views.login_controller.add_test_entry, name='add_test_entry'),
    url(r'^loginpost/test_history/(?P<pk>[0-9,a-z,A-Z,.,;,_]+)/$',views.login_controller.test_history, name='test_history'),
    url(r'^loginpost/test_delete/(?P<pk>[0-9,a-z,A-Z,.,;,_]+)/$',views.login_controller.test_delete, name='test_delete'),

    #url(r'^loginpost/test_show/(?P<pk>[0-9,a-z,A-Z,.,;,_]+)/$',views.login_controller.test_show, name='test_show'),

    #path('sign/', views.sign, name='sign')
]
