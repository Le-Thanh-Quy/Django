import random
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    context = {'a': current_time, 'list_random': range(10)}
    return render(request, 'CameraShop/view/index.html', context)
