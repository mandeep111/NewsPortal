from django.shortcuts import render

from django.views.generic import *
from .models import *

class HomeListView(ListView):
    template_name='home.html'
    model=News
    context_object_name='newslist'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categorys']=Category.objects.all()
        return context
