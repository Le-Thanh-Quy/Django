import random
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from .models import *


def index(request):
    list_camera = Camera.objects.all().order_by("-id")
    list_len = Lens.objects.all()

    context = {'list_camera': list_camera, 'list_len': list_len}
    return render(request, 'CameraShop/view/index.html', context)
