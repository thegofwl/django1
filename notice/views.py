from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def notice_web01(request):
    return HttpResponse('<h1> notice_web01 page </h1>')


def notice_web02(request):
    return HttpResponse('<h1> notice_web02 page </h1>')
