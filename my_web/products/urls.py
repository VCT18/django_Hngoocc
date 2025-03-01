from django.urls import path
from . import views
urlpatterns = [
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('category/<int:pk>', views.product_category, name='product_category'),
    path('store', views.store, name='store'),
    path('search', views.search, name='search'),
    path('filter', views.filter, name='filter'),
]