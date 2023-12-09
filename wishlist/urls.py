from django.urls import path, reverse_lazy, include
from django.views.generic import TemplateView

from . import views
from .views import *

urlpatterns = [
    path('a', views.index),
    path('', TemplateView.as_view(template_name='MainPage.html'), name='home'),
    path('users/', include('users.urls', namespace="users")),
    path('createlist', CreateList.as_view(), name='create'),
    path('list', ViewList.as_view(), name='list')
]