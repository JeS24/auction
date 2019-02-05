from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *

# Create your views here.

def live(request):
    product_live = Product.objects.filter(start_time__lte=datetime.now()).filter(end_time__gte=datetime.now())
    return render(request, 'host/live.html', {'product_live': product_live,})

def past(request):
    product_sold = Product.objects.filter(end_time__lte=datetime.now())
    return render(request, 'host/past.html', {'product_sold': product_sold,})

def all(request):
    product_list = Product.objects.order_by('end_time')
    return render(request, 'host/all.html', {'product_list': product_list,})

class Add(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'host/add.html'
