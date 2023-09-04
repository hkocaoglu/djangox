from typing import Any, Dict

from django.shortcuts import HttpResponse
from pages.models import Work
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Work
from .forms import WorkForm
from django.utils import timezone

class WorkListView(ListView):
    model = Work
    template_name = 'work/list.html'
    context_object_name = 'works'
    
class WorkDetailView(DetailView):
    model = Work
    template_name = 'work/detail2.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
   
    
class WorkCreateView(CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'work/form.html'
    success_url = reverse_lazy('work_list')
class WorkUpdateView(UpdateView):
    model = Work
    form_class = WorkForm
    template_name = 'work/form_edit.html'
    success_url = reverse_lazy('work_list')
   
class WorkDeleteView(DeleteView):
    model = Work
    template_name = 'work/confirm_delete.html'
    success_url = reverse_lazy('work_list')    
    
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class WorkTodayView(ListView):
    context_object_name = "work_list"
    queryset = Work.objects.filter(dateUpdate=timezone.now())
    template_name = "work/list2.html"

""" 
class WorkPageView(TemplateView):
     template_name = "pages/work.html"

class WorkDetailView(DetailView):
     model = Work
     
     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
          return super().get_context_data(**kwargs)
      
class WorkCreateView(CreateView):
    pass

from django.utils import timezone
from django.views.generic.list import ListView


class WorkListView(ListView):
    model = Work
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WorkCreateView(CreateView):
    model = Work
    fields = ["name"]
    template_name = "pages/work_create_form.html"
 """