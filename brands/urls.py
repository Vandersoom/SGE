from django.urls import path
from . import views



urlpatterns = [
    path('brands/list/', views.BrandlistView.as_view(), name='brand_list'),
]