
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.cemetery_list, name='cemetery_list'),

]

#url(r'^$',views.burial_list,name='burial-list'),