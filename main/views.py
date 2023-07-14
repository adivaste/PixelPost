''' Module to handle requests'''

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.forms import SignupForm, UploadForm
from main.models import Image
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    '''For Index page'''
    return render(request, 'main/index.html', {})


def user_login(request):
    '''For user login'''
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname  = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Logged in successfully !")
                    return HttpResponseRedirect('/profile')
        else:
            form = AuthenticationForm()
    else:
        return HttpResponseRedirect('/profile')
    return render(request, 'main/login.html', {'form': form})


def user_signup(request):
    '''For user signup'''
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created !")
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

def user_logout(request):
    ''' Log out User'''
    logout(request)
    return HttpResponseRedirect('/login')

# def profile(request):
#     '''For user profile'''
#     if request.user.is_authenticated:
#         all_image_objects = Image.objects.filter(account=get_user_model().objects.get(id=request.user.id).account)

#         image_data = [{'url': image_obj.image.url, 'title': image_obj.title} for image_obj in all_image_objects]
#         return render(request, 'main/profile.html', {'name': request.user, 'image_data': image_data})
#     else:
#         return HttpResponseRedirect('/login')
from django.db.models import Q

def profile(request):
    '''For user profile'''
    if request.user.is_authenticated:
        query = request.GET.get('search')  # Get the search query from the request
        all_image_objects = Image.objects.filter(account=get_user_model().objects.get(id=request.user.id).account)
        
        if query:
            # Filter images based on labels containing the search query
            all_image_objects = all_image_objects.filter(labels__name__icontains=query)
        
        image_data = [{'url': image_obj.image.url, 'title': image_obj.title, 'description': image_obj.description} for image_obj in all_image_objects]
        return render(request, 'main/profile.html', {'name': request.user, 'image_data': image_data})
    else:
        return HttpResponseRedirect('/login')



# def upload(request):
#     '''For upload images'''
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = UploadForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save(user=request.user)
#                 messages.success(request, "Image Uploaded Successfully !")
#         else:
#             form = UploadForm()
#     else:
#         return HttpResponseRedirect('/login')

#     return render(request, 'main/upload.html', {'form':form})

# FROM CHAT
def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            form.instance.request = request
            if form.is_valid():
                form.save(user=request.user)
                messages.success(request, "Image uploaded successfully!")
                return HttpResponseRedirect('/profile')
        else:
            form = UploadForm()
    else:
        return HttpResponseRedirect('/login')

    return render(request, 'main/upload.html', {'form': form})
