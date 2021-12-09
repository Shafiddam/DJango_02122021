from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

url_list = [
    "admin/",
    "horoscope/",
    "week_days/",
    "calc/"
]

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
