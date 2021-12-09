from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_square(request, width, height):
    sq = width*height
    return HttpResponse(f'Площадь равна = {sq}')