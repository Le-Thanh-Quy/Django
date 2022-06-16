import random
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

import CameraShop.models
from .models import *


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    context = {'a': current_time, 'list_random': range(10)}
    return render(request, 'CameraShop/view/index.html', context)

def order_page(request, user_id):
    list_item = Camera.objects.all()[:5]
    list_index = list(range(len(list_item)))
    list_image = []
    for item in list_item:
        list_image.append(Image.objects.get(id = item.image_id).productFrontImage.url)

    list_all = zip(list_index, list_item)

    # for index, item in li :

    json = '{"input_19_1001": {"price": "10", "quantityField": "input_19_quantity_1001_0", "custom_1": "input_19_custom_1001_1"}}'
    return render(request, 'CameraShop/view/order_page.html',
                  {"list_all": list_all,
                   "list_index": list_index,
                   "json": json})

def bill_page(request, user_id):
    list_item = Camera.objects.all()[:5]
    list_index = list(range(len(list_item)))
    list_image = []
    for item in list_item:
        list_image.append(Image.objects.get(id = item.image_id).productFrontImage.url)

    list_all = zip(list_index, list_item)

    # for index, item in li :

    json = '{"input_19_1001": {"price": "10", "quantityField": "input_19_quantity_1001_0", "custom_1": "input_19_custom_1001_1"}}'
    return render(request, 'CameraShop/view/bill_page.html',
                  {"list_all": list_all,
                   "list_index": list_index,
                   "json": json})


def history_page(request, user_id):
    list_item = Camera.objects.all()[:5]
    list_index = list(range(len(list_item)))
    list_image = []
    for item in list_item:
        list_image.append(Image.objects.get(id = item.image_id).productFrontImage.url)

    list_all = zip(list_index, list_item)

    # for index, item in li :

    json = '{"input_19_1001": {"price": "10", "quantityField": "input_19_quantity_1001_0", "custom_1": "input_19_custom_1001_1"}}'
    return render(request, 'CameraShop/view/history_page.html',
                  {"list_all": list_all,
                   "list_index": list_index,
                   "json": json})
