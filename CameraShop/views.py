import random
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, date
import re
from .models import *


def index(request):
    list_camera = Camera.objects.all().order_by("-id")
    list_camera = sorted(list_camera, key=lambda x: x.getStatus()[0], reverse=False)

    list_len = Lens.objects.all().order_by("-id")
    list_len = sorted(list_len, key=lambda x: x.getStatus()[0], reverse=False)

    list_slides = [x for x in list_camera if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]
    slide_center_index = len(list_slides)
    list_slides = list_slides + [x for x in list_len if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]

    context = {
        'list_camera': list_camera,
        'list_len': list_len,
        'list_slides': list_slides,
        'is_search': False,
        'slide_center_index': slide_center_index,
        'request': request
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
    slide_center_index = len(list_slides)
    list_slides = list_slides + [x for x in list_len if x.getStatus()[0] == 0 or x.getStatus()[0] == 1]

    context = {
        'list_camera': list_camera,
        'list_len': list_len,
        'list_slides': list_slides,
        'is_search': True,
        'content_search': content,
        'slide_center_index': slide_center_index,
        'request': request
    }
    return render(request, 'CameraShop/view/index.html', context)


def detail_camera(request, id_camera):
    product = Camera.objects.get(id=id_camera)

    list_camera = Camera.objects.all().order_by("-id")
    list_camera = sorted(list_camera, key=lambda x: x.getStatus()[0], reverse=False)
    list_camera = [x for x in list_camera if str(x.lensMount).upper().find(str(product.lensMount).upper()) != -1]

    list_len = Lens.objects.all().order_by("-id")
    list_len = sorted(list_len, key=lambda x: x.getStatus()[0], reverse=False)
    list_len = [x for x in list_len if str(x.lensMount).upper().find(str(product.lensMount).upper()) != -1]

    context = {
        'camera': product,
        'list_camera': list_camera,
        'list_len': list_len,
        'request': request,
    }
    return render(request, 'CameraShop/view/detail.html', context)


def detail_len(request, id_len):
    product = Lens.objects.get(id=id_len)

    list_camera = Camera.objects.all().order_by("-id")
    list_camera = sorted(list_camera, key=lambda x: x.getStatus()[0], reverse=False)
    list_camera = [x for x in list_camera if str(x.lensMount).upper().find(str(product.lensMount).upper()) != -1]

    list_len = Lens.objects.all().order_by("-id")
    list_len = sorted(list_len, key=lambda x: x.getStatus()[0], reverse=False)
    list_len = [x for x in list_len if str(x.lensMount).upper().find(str(product.lensMount).upper()) != -1]

    context = {
        'len': product,
        'list_camera': list_camera,
        'list_len': list_len,
        'request': request,
    }
    return render(request, 'CameraShop/view/detail.html', context)


def login(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("signin"):
            user_name = request.POST.get("user_name")
            password = request.POST.get("your_pass")

            if not str(user_name).strip() or not str(password).strip():
                context = {'isWrong': True, 'notification': "Please enter all fields"}
            elif User.objects.filter(account=str(user_name).strip()).exists():
                user = User.objects.filter(account=str(user_name).strip())[0]
                if user.password == password:
                    request.session["isAuth"] = user_name
                    return index(request)
                else:
                    context = {'isWrong': True, 'notification': "Incorrect username or password"}
            else:
                context = {'isWrong': True, 'notification': "Incorrect username or password"}
    return render(request, 'CameraShop/view/login.html', context)


def validNumber(phone_nuber):
    valid_number = "^[+|0]{1}[0-9]{9,11}$"
    pattern = re.compile(valid_number, re.IGNORECASE)
    return pattern.match(phone_nuber) is not None


def register(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("signup"):
            user_name = request.POST.get("name")
            password = request.POST.get("pass")
            re_password = request.POST.get("re_pass")
            full_name = request.POST.get("full_name")
            phone_number = request.POST.get("phone")
            birth_date = request.POST.get("birthday")
            address = request.POST.get("address")
            if not str(user_name).strip() or not str(password).strip() or not str(re_password).strip() or not str(
                    full_name).strip() or not str(phone_number).strip() or not str(birth_date).strip() or not str(
                address).strip():
                context = {'isWrong': True, 'notification': "Please enter all fields"}
            elif str(password).strip() != str(re_password).strip():
                context = {'isWrong': True, 'notification': "Password does not match"}
            elif len(str(password).strip()) < 6:
                context = {'isWrong': True, 'notification': "Passwords must be at least 6 characters"}
            elif not validNumber(str(phone_number)):
                context = {'isWrong': True, 'notification': "Invalid phone number"}
            elif User.objects.filter(account=str(user_name).strip()).exists():
                context = {'isWrong': True, 'notification': "Account already exists"}
            else:
                user = User(name=full_name, password=password, account=user_name, dateOfBirth=birth_date,
                            phoneNumber=phone_number, address=address)
                user.save()
                context = {
                    'isSuccessful': True,
                    'notification': "Create Account Success",
                    'user_name': str(user_name).strip(),
                    'pass_word': str(password).strip()
                }
                return render(request, 'CameraShop/view/login.html', context)
    return render(request, 'CameraShop/view/register.html', context)


def profile(request, user_name):
    user = User.objects.filter(account=user_name)[0]
    context = {
        'user': user,
        'request': request,
    }
    return render(request, 'CameraShop/view/profile.html', context)


def logout(request):
    context = {}
    try:
        del request.session['isAuth']
        context = {'isWrong': True, 'notification': 'Sign out successful'}
    except KeyError:
        pass
    return render(request, 'CameraShop/view/login.html', context)
