from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page with Search
    path('prompt/<int:pk>/', views.prompt_detail, name='prompt_detail'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('settings/', views.profile_settings, name='profile_settings'),
]
