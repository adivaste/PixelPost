''' Module to handle requests'''

from django.shortcuts import render

# Create your views here.
def index(request):
    '''For Index page'''
    return render(request, 'main/index.html', {})


def user_login(request):
    '''For user login'''
    return render(request, 'main/login.html', {})


def user_signup(request):
    '''For user signup'''
    return render(request, 'main/signup.html', {})


def profile(request, username):
    '''For user profile'''
    return render(request, 'main/profile.html', {"username" : username})


def upload(request):
    '''For upload images'''
    return render(request, 'main/upload.html', {})
