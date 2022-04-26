from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('success', IndexView.as_view(), name="success"),
    path('fail', IndexView.as_view(), name="fail"),
    path('export/', views.csvexport, name='csvexport'),
]