import random
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, date

from .models import *


def index(request):
    # for camera in Camera.objects.all():
    #     obj = Camera.objects.get(id=camera.id)
    #     obj.quantityInStock = 9
    #     obj.save()
    list_camera = Camera.objects.all().order_by("-id")
    list_camera = sorted(list_camera, key=lambda x: x.getStatus()[0], reverse=False)

    list_len = Lens.objects.all().order_by("-id")
    list_len = sorted(list_len, key=lambda x: x.getStatus()[0], reverse=False)

    list_slides = [x for x in list_camera if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]
    list_slides = list_slides + [x for x in list_len if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]

    context = {
        'list_camera': list_camera,
        'list_len': list_len,
        'list_slides': list_slides,
        'is_search': False
    }
    return render(request, 'CameraShop/view/index.html', context)


def search(request, content):
    list_camera = Camera.objects.all().order_by("-id")
    list_camera = sorted(list_camera, key=lambda x: x.getStatus()[0], reverse=False)
    list_camera = [x for x in list_camera if x.name.upper().find(str(content).upper()) != -1]

    list_len = Lens.objects.all().order_by("-id")
    list_len = sorted(list_len, key=lambda x: x.getStatus()[0], reverse=False)
    list_len = [x for x in list_len if x.name.upper().find(str(content).upper()) != -1]

    list_slides = [x for x in list_camera if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]
    list_slides = list_slides + [x for x in list_len if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]

    context = {
        'list_camera': list_camera,
        'list_len': list_len,
        'list_slides': list_slides,
        'is_search': True,
        'content_search': content
    }
    return render(request, 'CameraShop/view/index.html', context)
