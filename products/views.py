
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'


def product_list(request):
    queryset = Product.objects.all()
    context = {
         'object_list': queryset
         }
    return render(request, 'products/product_list.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'


def product_detail(request):
    #instance = Product.objects.get(pk=id)
    instance = get_object_or_404(Product, pk=id)
    context = {
         'object': instance
         }
    return render(request, 'products/product_detail.html', context)
