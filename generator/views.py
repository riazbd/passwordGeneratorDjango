from django.shortcuts import render
# from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def yourpassword(request):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('uppercase'):
        chars.extend([x.upper() for x in chars])
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()[]{}"\';:.,?/\\|'))
    if request.GET.get('number'):
        chars.extend(list('0123456789'))
    length = int(request.GET.get('length', 8))
    thepass = ""
    for values in range(length):
        thepass += random.choice(chars)
    return render(request, "generator/password.html", {'password': thepass})
