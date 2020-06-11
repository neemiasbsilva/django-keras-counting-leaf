from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Regression


# Create your views here.
class RegressionListView(ListView):
    model = Regression
    template_name = 'cnn_counting_leaf/list.html'
    context_object_name = 'items'


class RegressionCreateView(CreateView):
    model = Regression
    fields = ['img']


class RegressionUpdateView(UpdateView):
    model = Regression
    fields = ['img']


class RegressionDeleteView(DeleteView):
    model = Regression
    success_url = '/'
