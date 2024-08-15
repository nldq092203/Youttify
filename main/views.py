from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from youttify_auth.models import YouttifyUser
from django.urls.base import reverse
from django.contrib.auth import authenticate,login,logout
from youtube_search import YoutubeSearch
import json
# import cardupdate



f = open('card.json', 'r')
CONTAINER = json.load(f)

def default(request):
    global CONTAINER


    if request.method == 'POST':
        return HttpResponse("")

    song = 'kSFJGEHDCrQ'
    return render(request, 'main/home.html',{'CONTAINER':CONTAINER, 'song':song})



