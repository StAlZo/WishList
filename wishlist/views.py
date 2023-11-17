from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(requerst):
    #return HttpResponse("wishlist")
    return render(requerst, 'MainPage.html')


def login(requerst):
    return render(requerst, 'login.html')