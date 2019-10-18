from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


class ProductFeatureListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all().featured()


class ProductFeatureDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/product_feature_detail.html'

    # def get_queryset(self):
    #   request = self.request
    #  return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all()


def product_list(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug)  # Product.objects.get(slug=slug)
        if instance is None:
            raise Http404('Product doesn`t exist')
        return instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        return context

    # def get_object(self, *args, **kwargs):
    #   request = self.request
    #  pk = self.kwargs.get('pk')
    # instance = Product.objects.get_by_id(pk)
    # if instance is None:
    #   raise Http404('Product doesn`t exist')
    # return instance

    def get_queryset(self):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


def product_detail(request):
    qs = Product.objects.filter(id=id)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404('Product doesn`t exist')
    context = {
        'object': instance
    }
    return render(request, 'products/product_detail.html', context)
