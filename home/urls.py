from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.index, name='index'),
    path('loginpost/', views.loginpost, name='loginpost'),
    path('speedometer/', views.speedometer, name='speedometer'),
    path('app/', views.app, name='app'),
    path('datatable_update/', views.datatable_update, name='datatable_update'),

    #path('sign/', views.sign, name='sign')
]
