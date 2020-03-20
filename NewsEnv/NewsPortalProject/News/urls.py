from django.urls import path
from django.conf.urls.static import static
from News import views
app_name='News'
from .views import *

urlpatterns=[
    path('',views.index,name='home'),
    path('detail/<int:pk>', NewsDetailView.as_view(), name='newsdetail'),
    path('blog/<int:pk>/',BlogView.as_view(),name='blog'),
    path('detail', views.createcomment, name='newsdetail')
  
]