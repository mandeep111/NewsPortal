from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from News import views
from .models import *
from django.core.paginator import Paginator

class ClientMixin(object):
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categorys']=Category.objects.all()
        context['latestnews']=News.objects.order_by('-id')
        return context





# class HomeListView(ListView):
#     template_name='home.html'
#     model=News
#     context_object_name='newslist'

#     def get_context_data(self,*args,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context['news']=News.objects.all()
#         context['categorys'] = Category.objects.all()
#         return context
def index(request):
    shelf = News.objects.all()
    latestnews=News.objects.order_by('-id')
    category = Category.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(shelf, 4)
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html', {'shelf': page_obj, 'categorys': category,'latestnews':latestnews})



class BlogView(ClientMixin,TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.all()
        category_id = self.kwargs['pk']
        category = Category.objects.get(id=category_id)
        print(category, 'ram')
        context['category'] = category
        context['news'] = news
        return context


class NewsDetailView(ClientMixin,DetailView):
    template_name = 'detail.html'
    model = News
    context_object_name = 'news'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        news_id = self.kwargs['pk']
        news = News.objects.get(id=news_id)
        news.views_count += 1
        news.save()
        return context



