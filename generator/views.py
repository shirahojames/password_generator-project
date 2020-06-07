from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

# Create your views here.

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'generator/time.html', {'timezones': pytz.common_timezones})

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*?'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length','12'))

    thepassword = ''
    for x in range(length):

        thepassword+= random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
