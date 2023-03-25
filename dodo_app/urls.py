
from django.urls import path

from dodo_app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("index",views.index,name="index"),
    path("indexx",views.indexx,name="indexx"),
    path("add",views.add,name="view"),
    path("getdata",views.getdata,name="getdata"),
    path('update/<int:Todo_id>/',views.update,name="update"),
    path('delete/<int:Todo_id>/',views.delete,name="delete")
]