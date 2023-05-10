from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name='home.html'),
    path("data/",views.data,name='data.html'),
    path ("data/<int:id>",views.data_list,name='data_list'),
   
   
]