from django.urls import path, reverse_lazy

from . import views
from .views import *

urlpatterns = [
    path('', views.index)
]