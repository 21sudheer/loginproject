from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import User
from webapp.forms import webform
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import sys


# Create your views here.
def HomePage(request):
    # return redirect("/HomePage")
    return render(request, "home.html")


@csrf_exempt
def register(request):
    print("hi")
    form = webform()
    if request.method == "POST":
        print("hello")
        print(request.POST)

        uname = request.POST.get("name")
        phonenumber = request.POST.get("phone_number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        pass2 = request.POST.get("password2")

        my_user = authenticate(email=email, password=password)
        print(my_user)

        # if my_user:
        #     user_exists = False
        #     raise ValidationError("email already exists")
        # else:
        #     user_exists = True
        #     print("hello", user_exists)
        #     return render(request, "register.html", {"user_exists": user_exists})

        try:
            print("enters")
            if password != pass2:
                raise Exception
        except Exception:
            sys.exit()

        else:
            print(uname)
            print(phonenumber)
            print(email)
        print("middle")
        form = webform(request.POST)
        # print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print("enters")
            form.save()
            return redirect("/")
            # return HttpResponse("data inserted")

    return render(request, "register.html", {"form": form})


@csrf_exempt
def LoginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        print(email)
        print(pass1)
        my_user = authenticate(email=email, password=pass1)
        if my_user:
            user_not_exists = False
            user = User.objects.get(email=my_user)
            login(request, user)
            print("jjjj")
            return redirect("/HomePage")

        else:
            user_not_exists = True
            # output = "user does not exist"
            # d1 = {"result": output}
            # return JsonResponse(d1)
            print("hello", user_not_exists)
            return render(request, "login.html", {"user_not_exists": user_not_exists})

        # if my_user:
        #     print("jjjj")
        #     return redirect("/HomePage")

    return render(request, "login.html")


def logoutPage(request):
    logout(request)
    return redirect("/")
    # return render(request, "login.html")
