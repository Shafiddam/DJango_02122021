from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
import math

figure_list = ["Прямоугольник", "Квадрат", "Круг"]
def index(request):  # ГЛАВНАЯ СТРАНИЦА С МЕНЮ
    li_elements = ''
    for word in figure_list:
        redirect_path = reverse('horoscope-name', args=[word])
        li_elements += f'<li> <a href= {word}> {word.title()} </a> </li>'
    response = f"""
    <ul>
        {li_elements}
             
    </ul>
    """
    return HttpResponse(response)


def get_rectangle_area(request, width, height):
    sq = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width} на {height} равна = {sq}')


def get_square_area(request, width):
    sq = width ** 2
    return HttpResponse(f'Площадь квадрата со стороной {width} равна = {sq}')


def get_circle_area(request, radius):
    sq = math.pi * radius ** 2
    return HttpResponse(f'Площадь круга радиуса {radius} равна = {sq}')
