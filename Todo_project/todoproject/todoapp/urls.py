from django.contrib import admin
from django.urls import path, include
from . import views

app_name='todoapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.tasklistview.as_view(), name='cvbhome'),
    path('cbvdetails/<int:pk>/',views.taskdetailview.as_view(),name='cbvdetailview'),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cbvdelete'),
    # path('details/',views.details,name='details'),
]
