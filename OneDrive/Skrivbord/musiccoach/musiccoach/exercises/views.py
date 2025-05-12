from django.shortcuts import render

from django.http import HttpResponse


def exercises(request):
    return HttpResponse("Hello world!")
