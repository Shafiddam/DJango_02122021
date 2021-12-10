from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    "Овен": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)", #0 Fire
    "Телец": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",  #1 Earth
    "Близнецы": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)", #2
    "Рак": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)", #3
    "Лев": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)", #4 Fire
    "Дева": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)", #5 Earth
    "Весы": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)", #6
    "Скорпион": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)", #7
    "Стрелец": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)", #8 Fire
    "Козерог": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января", #9 Earth
    "Водолей": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)", #10
    "Рыбы": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)" #11
}


def index(request): #ГОРОСКОП - ГЛАВНАЯ СТРАНИЦА С МЕНЮ
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f'<li> <a href= {redirect_path} > {sign.title()} </a> </li>'
    response = f"""
    <ol>
        {li_elements}
             <a href= {type} type </a>
    </ol>
    
    """
    return HttpResponse(response)


def type(request):  #ВЕРНУТЬ в состояние просто type!
    type_list = ["Fire", "Earth", "Air", "Water"]
    li_urls = ''
    for x in type_list:
        li_urls += f'<li> <a href= {x}> {x} </a> </li>'
    response = f"""
        <ul>
            {li_urls}
        </ul>
        """
    return HttpResponse(response)


# def type(request):
#     fire = list(zodiac_dict)[0:12:4]
#     return HttpResponse(fire )


def type_Fire(request):
    fire_list = ["Овен", "Лев", "Стрелец"]
    li_urls = ''
    for x in fire_list:
        redirect_path = reverse('horoscope-name', args=[x])
        li_urls += f'<li> <a href= {redirect_path}> {x} </a> </li>'
    response = f"""
        <ul>
            {li_urls}
        </ul>
        """
    return HttpResponse(response)


def type_Earth(request):
    earth_list = ["Телец", "Дева", "Козерог"]
    li_urls = ''
    for x in earth_list:
        redirect_path = reverse('horoscope-name', args=[x])
        li_urls += f'<li> <a href= {redirect_path}> {x} </a> </li>'
    response = f"""
        <ul>
            {li_urls}
        </ul>
        """
    return HttpResponse(response)


def type_Air(request):
    air_list = ["Близнецы", "Весы", "Водолей"]
    li_urls = ''
    for x in air_list:
        redirect_path = reverse('horoscope-name', args=[x])
        li_urls += f'<li> <a href= {redirect_path}> {x} </a> </li>'
    response = f"""
        <ul>
            {li_urls}
        </ul>
        """
    return HttpResponse(response)


def type_Water(request):
    water_list = ["Рак", "Скорпион", "Рыбы"]
    li_urls = ''
    for x in water_list:
        redirect_path = reverse('horoscope-name', args=[x])
        li_urls += f'<li> <a href= {redirect_path}> {x} </a> </li>'
    response = f"""
        <ul>
            {li_urls}
        </ul>
        """
    return HttpResponse(response)


'''
# Блок с выводом вместо имен просто цифры знаков
def type_Fire(request):    
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for x in range(0, len(zodiacs), 4):
        redirect_path = reverse('horoscope-name', args=[x+1])
        li_elements += f'<li> <a href= {redirect_path} > {x+1} </a> </li>'
    response = f"""
        <ul>
            {li_elements}
        </ul>

        """
    return HttpResponse(response)
'''

# def type_Fire(request):
#     # zodiacs = zodiac_dict # преобразуем словарь в список
#     # for x in range(0, len(zodiacs), 4):
#     # for x in index(zodiacs):
#     return HttpResponse(zodiac_dict)



def get_info_about_type_zodiac(request, type_zodiac):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Нет такого знака {sign_zodiac} ')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака {sign_zodiac} ')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Нет такого знака {sign_zodiac} ')

def get_sign_zodiac(request, day: int, month: int):
    zodiacs = list(zodiac_dict)
    if month == 1 and day <= 19 or month == 12 and day >= 22:
        return HttpResponse(zodiacs[9])
    if month == 2 and day <= 18 or month == 1 and day >= 20:
        return HttpResponse(zodiacs[10])
    if month == 3 and day <= 20 or month == 2 and day >= 19:
        return HttpResponse(zodiacs[11])
    if month == 4 and day <= 19 or month == 3 and day >= 21:
        return HttpResponse(zodiacs[0])
    if month == 5 and day <= 20 or month == 4 and day >= 20:
        return HttpResponse(zodiacs[1])
    if month == 6 and day <= 20 or month == 5 and day >= 21:
        return HttpResponse(zodiacs[2])
    if month == 7 and day <= 22 or month == 6 and day >= 21:
        return HttpResponse(zodiacs[3])
    if month == 8 and day <= 22 or month == 7 and day >= 23:
        return HttpResponse(zodiacs[4])
    if month == 9 and day <= 22 or month == 8 and day >= 23:
        return HttpResponse(zodiacs[5])
    if month == 10 and day <= 22 or month == 9 and day >= 23:
        return HttpResponse(zodiacs[6])
    if month == 11 and day <= 21 or month == 10 and day >= 23:
        return HttpResponse(zodiacs[7])
    if month == 12 and day <= 21 or month == 11 and day >= 22:
        return HttpResponse(zodiacs[8])