
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^cemetery/', views.cemetery, name='cemetery'),
    url(r'^add_cemetery/', views.add_cemetery, name='add_cemetery'),
    url(r'^view_cemetery/', views.view_cemetery, name='view_cemetery'),
    url(r'^edit_cemetery/', views.edit_cemetery, name='edit_cemetery'),
    url(r'^delete_cemetery/', views.delete_cemetery, name='delete_cemetery'),
    url(r'^burial/', views.burial, name='burial'),
    url(r'^add_burial/', views.add_burial, name='add_burial'),
    url(r'^view_burial/', views.view_burial, name='view_burial'),
    url(r'^edit_burial/', views.edit_burial, name='edit_burial'),
    url(r'^delete_burial/', views.delete_burial, name='delete_burial'),
    url(r'^photo/', views.photo, name='photo'),
    url(r'^add_photo/', views.add_photo, name='add_photo'),
    url(r'^view_photo/', views.view_photo, name='view_photo'),
    url(r'^edit_photo/', views.edit_photo, name='edit_photo'),
    url(r'^delete_photo/', views.delete_photo, name='delete_photo'),
    url(r'^add/', views.add, name='add'),
    url(r'^view/', views.view, name='view'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^delete/', views.delete, name='delete'),
]
