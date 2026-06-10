from django.shortcuts import render
from django.http import HttpResponse , JsonResponse    #پاسخ دادن به کاربر



def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def about_view(request):
    return HttpResponse('<h1>About Page</h1>')

def contact_view(request):
    return HttpResponse('<h1>Cantact Page</h1>')

