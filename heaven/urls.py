
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^cemetery/', views.cemetery, name='cemetery'),
    url(r'^cemetery_list/', views.cemetery_list, name='cemetery_list'),
    url(r'^burial/', views.burial, name='burial'),
    url(r'^burial_list/', views.burial_list, name='burial_list'),
]

# url(r'^$', views.cemetery_list, name='cemetery_list'),
#url(r'^$',views.burial_list,name='burial-list'),