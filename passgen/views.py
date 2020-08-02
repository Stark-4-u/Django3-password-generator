from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def hello(request):
    return render(request,'passgen/home.html')
def password(optimus):
    testpassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if optimus.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if optimus.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if optimus.GET.get('special'):
        characters.extend(list('!@#$_'))

    length  = int(optimus.GET.get('length',10))

    for x in range(length):
        testpassword += random.choice(characters)


    return render(optimus,'passgen/password.html',{'password':testpassword})

def about(request):
    return render(request,'passgen/about.html')
