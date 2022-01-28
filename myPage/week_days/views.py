from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_info_about_week_days(request, week_days):
    if week_days == 'понедельник' or week_days == '1':
        return render(request, 'week_days/greeting.html')

        # return HttpResponse('<!DOCTYPE html>  <html lang="ru">'
        #                     '    <h2>Страница <font  color = red > ПОНЕДЕЛЬНИК </font></h2>'
        #                     '<p style="text-indent:20px">'
        #                     '</html>')

    # if week_days == 'вторник' or week_days == '2':
    #     return HttpResponse('<!DOCTYPE html>  <html lang="ru">'
    #                         '    <h2>Страница ВТОРНИК</h2>'
    #                         '<p style="text-indent:20px">'
    #                         '</html>')
    else:
        return HttpResponseNotFound ('Нет такого дня недели')


