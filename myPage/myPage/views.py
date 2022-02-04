from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# ----------------------- Самая ПЕРВАЯ Главная страница --------------------------------

url_list = [
    "Admin",
    "Гороскоп", # "horoscope/",
    "Ежедневник", # "geometry/",
    "Калькулятор", #"calc/",
    # "Типы_стихий", #"type/"
    "Площадь_фигур", # geometry2/
]

# ----------------------- вывод в виде списка на главной странице --------------------------------
def index(request):
    li_urls = ''
    for x in url_list:
        li_urls += f'<li> <a href= {x}> {x.title()} </a> </li>'
    response = f"""
        <ul>
            {li_urls}
        </ul>
        """
    return HttpResponse(response)
