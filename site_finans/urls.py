from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recursos/', views.recursos),
    path('beneficios/', views.beneficios),
    path('try/', views.test),
    path('results/', views.test),
    path('about/', views.about),
]