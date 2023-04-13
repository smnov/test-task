from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('api/text-form/', views.post_data)
]