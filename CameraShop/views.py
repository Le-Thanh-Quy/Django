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

    list_camera_all = Camera.objects.all().order_by("-id")
    list_camera = [x for x in list_camera_all if str(x.lensMount).upper().find(str(product.lensMount).upper()) != -1]
    list_camera = set(
        list_camera + [x for x in list_camera_all if str(x.company).upper().find(str(product.company).upper()) != -1])
    list_camera = sorted(list_camera, key=lambda x: x.getStatus()[0], reverse=False)

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

    list_len_all = Lens.objects.all().order_by("-id")
    list_len = [x for x in list_len_all if str(x.lensMount).upper().find(str(product.lensMount).upper()) != -1]
    list_len = set(
        list_len + [x for x in list_len_all if str(x.lensFormat).upper().find(str(product.lensFormat).upper()) != -1])
    list_len = sorted(list_len, key=lambda x: x.getStatus()[0], reverse=False)

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
            birthday = request.POST.get("birthday")
            address = request.POST.get("address")
            if not str(user_name).strip() or not str(password).strip() or not str(re_password).strip() or not str(
                    full_name).strip() or not str(phone_number).strip() or not str(birthday).strip() or not str(
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
                user = User(name=full_name, password=password, account=user_name, dateOfBirth=birthday,
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
    context = {}
    is_notification = False
    is_modal = False
    notification = ""
    if request.method == "POST":
        if request.POST.get("update-profile"):
            password = request.POST.get("password")
            full_name = request.POST.get("name")
            phone_number = request.POST.get("phone")
            birthday = request.POST.get("birthday")
            address = request.POST.get("address")
            gender = request.POST.get("gender")
            if not str(password).strip() or not str(full_name).strip() or not str(phone_number).strip() or not str(
                    birthday).strip() or not str(
                    address).strip() or not str(gender).strip():
                is_notification = True
                notification = "Please enter all fields"
            elif not validNumber(str(phone_number)):
                is_notification = True
                notification = "Invalid phone number"
            else:
                new_user = User.objects.filter(account=user_name)[0]
                if gender == "female":
                    new_user.gender = "Female"
                else:
                    new_user.gender = "Male"
                new_user.name = full_name
                new_user.address = address
                new_user.dateOfBirth = birthday
                new_user.phoneNumber = phone_number
                new_user.save()
                is_notification = True
                notification = "Update successful"
        elif request.POST.get("reset-password"):
            is_modal = True
            current_password = request.POST.get("current-password")
            new_password = request.POST.get("new-password")
            confirm_password = request.POST.get("confirm-password")
            user_password = User.objects.filter(account=user_name)[0].password
            if not str(current_password).strip() or not str(new_password).strip() or not str(confirm_password).strip():
                is_notification = True
                notification = "Please enter all fields"
            elif not str(new_password) == str(confirm_password):
                is_notification = True
                notification = "Password does not match"
            elif len(str(new_password).strip()) < 6:
                is_notification = True
                notification = "Passwords must be at least 6 characters"
            elif not str(current_password) == str(user_password):
                is_notification = True
                notification = "Current password does not match"
            else:
                new_user = User.objects.filter(account=user_name)[0]
                new_user.password = new_password
                new_user.save()
                is_notification = True
                notification = "Update successful"
                is_modal = False

    user = User.objects.filter(account=user_name)[0]
    user.password = "*" * len(user.password)
    date_of_birth = user.dateOfBirth
    year = str(date_of_birth.year)
    moth = str(date_of_birth.month)
    day = str(date_of_birth.day)
    if int(moth) < 10:
        moth = '0' + moth
    if int(day) < 10:
        day = '0' + day
    date_of_birth = year + '-' + moth + '-' + day
    context = {
        'user': user,
        'dateOfBirth': date_of_birth,
        'request': request,
        'isWrong': is_notification,
        'notification': notification,
        'is_modal': is_modal
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
