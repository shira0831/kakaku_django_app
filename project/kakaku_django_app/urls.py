from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('export/', views.csvexport, name='csvexport'),
]