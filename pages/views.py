from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Page

# Create your views here.
class PageListView(ListView):
  model = Page
  template_name = 'pages/pages_list.html'
   
class PageDetailView(DetailView):
  model = Page
  template_name = 'pages/page_detail.html'
  
class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    
    def get_success_url(self):
      return reverse('pages:pages')