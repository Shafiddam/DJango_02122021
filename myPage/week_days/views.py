from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


def get_info_about_week_days(request):
    return render(request, 'week_days/greeting.html')
    # return render(request, 'week_days/greeting.html')

    # return HttpResponse('<!DOCTYPE html>  <html lang="ru">'
    #                     '    <h2>Страница <font  color = red > ПОНЕДЕЛЬНИК </font></h2>'
    #                     '<p style="text-indent:20px">'
    #                     '</html>')

    # if geometry == 'вторник' or geometry == '2':
    #     return HttpResponse('<!DOCTYPE html>  <html lang="ru">'
    #                         '    <h2>Страница ВТОРНИК</h2>'
    #                         '<p style="text-indent:20px">'
    #                         '</html>')

    # else:
    #     return HttpResponseNotFound ('Нет такого дня недели')


