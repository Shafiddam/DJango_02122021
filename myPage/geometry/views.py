from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
import math

# figure_list = ["Прямоугольник", "Квадрат", "Круг"]
def index(request):  # ГЛАВНАЯ СТРАНИЦА С МЕНЮ ФИГУР
    return render(request, 'geometry/base.html')
    # li_elements = ''
    # for word in figure_list:
    #     redirect_path = reverse('horoscope-name', args=[word])
    #     li_elements += f'<li> <a href= {word}> {word.title()} </a> </li>'
    # response = f"""
    # <ul>
    #     {li_elements}
    #
    # </ul>
    # """
    # return HttpResponse(response)


# def get_rectangle_area(request, width, height):
#     sq = width * height
#     return HttpResponse(f'Площадь прямоугольника размером {width} на {height} равна = {sq}')
def rectangle_area(request):
    return render(request, 'geometry/rectangle.html')


# def square_area(request, width):
def square_area(request):
    # sq = width ** 2
    # return HttpResponse(f'Площадь квадрата со стороной {width} равна = {sq}')
    return render(request, 'geometry/square.html')


# def circle_area(request, radius):
def circle_area(request):
    # sq = math.pi * radius ** 2
    # return HttpResponse(f'Площадь круга радиуса {radius} равна = {sq}')
    return render(request, 'geometry/circle.html')