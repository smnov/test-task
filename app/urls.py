from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/texts', views.Index.as_view())
]