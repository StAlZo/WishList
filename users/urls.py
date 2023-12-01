from django.contrib import admin
from django.urls import path, include
from users.views import LoginUser
from django.contrib.auth.views import LogoutView
from DreamBoard import settings
from users.views import Register

app_name = "users"

urlpatterns = [


    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),

]
#path('registration/', SignUpView.as_view(), name='registrations'),
#path('login/', LoginUser.as_view(), name='login'),
#path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),