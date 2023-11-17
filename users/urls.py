from django.contrib import admin
from django.urls import path, include
from users.views import SignUpView, LoginUser
from django.contrib.auth.views import LogoutView
from DreamBoard import settings

urlpatterns = [
    path('registration/', SignUpView.as_view(), name='registrations'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]