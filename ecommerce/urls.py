"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import (
    ProductListView, product_list, ProductDetailView, product_detail,
    ProductFeatureListView, ProductFeatureDetailView,
    ProductDetailSlugView,
                            )
from .views import *


urlpatterns = [
    path('', home_page, ),
    path('admin/', admin.site.urls),
    path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('product/', ProductListView.as_view()),
    path('product-fbv/', product_list),
    #path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/<str:slug>/', ProductDetailSlugView.as_view()),
    path('product-d/', product_detail),
    path('feature/<int:pk>/', ProductFeatureDetailView.as_view()),
    path('feature/', ProductFeatureListView.as_view()),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

