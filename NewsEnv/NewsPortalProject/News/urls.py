from django.urls import path
app_name='News'
from .views import *

urlpatterns=[
    path('',HomeListView.as_view(),name='home')
]