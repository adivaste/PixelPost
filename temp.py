# import requests
# import os

# api_key = 'acc_23c683b3a6a6147'
# api_secret = 'c45920b2b1e0885dbc39958a084ee6a4'
# image_url = 'https://pixelpost.pythonanywhere.com/media/images/image_4.jpg'

# response = requests.get(
#     'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
#     auth=(api_key, api_secret))

# print(response.json())

# # import requests
# # import os

# # response = requests.get("http://localhost:8000/media/images/cloud-data_r1ZNOtcI.png")

# import requests
# import json

# def basic_upload(account_id, api_key, file_data, metadata=None, querystring=None):
#     base_url = "https://api.upload.io"
#     path = f"/v2/accounts/{account_id}/uploads/binary"

#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "X-Upload-Metadata": json.dumps(metadata) if metadata else None
#     }

#     files = {"file": file_data}

#     response = requests.post(
#         f"{base_url}{path}",
#         headers=headers,
#         files=files,
#         params=querystring
#     )

#     result = response.json()
#     if response.status_code // 100 != 2:
#         raise Exception(f"Upload API Error: {json.dumps(result)}")

#     return result

# # Example usage
# account_id = "W142i4y"
# api_key = "public_W142i4yo25Mx5USrQgPKcBZa5x6J"
# file_data = open("./pexels-pixabay-60597.jpg", "rb")
# metadata = {
#     "myCustomField1": True,
#     "myCustomField2": {"hello": "world"},
#     "anotherCustomField": 42
# }
# querystring = {
#     "fileName": "image.jpg",
#     "fileNameFallback": "image.jpg",
#     "fileNameVariablesEnabled": True,
#     "filePath": "/uploads/image.jpg",
#     "folderPath": "/uploads",
#     "folderPathVariablesEnabled": True,
#     "originalFileName": "example.jpg",
#     "tag": ["example_tag"]
# }

# try:
#     response = basic_upload(account_id, api_key, file_data, metadata, querystring)
#     print(f"Success: {json.dumps(response)}")
# except Exception as e:
#     print(f"Error: {str(e)}")
# finally:
#     file_data.close()

import cloudinary
import cloudinary.uploader

# Configure Cloudinary with your credentials
cloudinary.config( 
  cloud_name = "dpko5pze5", 
  api_key = "376313185274629", 
  api_secret = "-S6eX5EuUPKcirZco0_K4z8AC70" 
)

# Example: Upload an image
image_path = './pexels-pixabay-60597.jpg'
uploaded_image = cloudinary.uploader.upload(image_path)
print(uploaded_image['secure_url'])





from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from main.models import Image, Account, Label
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import requests
from django.conf import settings
import time

class SignupForm(UserCreationForm):
    # gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect)
    # avatar = forms.ImageField(required=True)

    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.Select(attrs={'class': 'form-check-input'}))
    avatar = forms.ImageField(required=False)
    # widget=forms.FileInput(attrs={'class': 'form-control-file'}

    class Meta:
        model = User
        fields  = ('username', 'email', 'first_name', 'last_name', 'gender', 'avatar')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
        }


    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            account = Account.objects.create(
                user=user,
                gender=self.cleaned_data['gender'],
                avatar = self.cleaned_data['avatar']
            )
            account.save()


# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'description', 'image')

#     def save(self, commit=True, user=None):
#         instance = super().save(commit=False)
#         if user:
#             instance.account = get_user_model().objects.get(id=user.id).account
#         if commit:
#             instance.save()

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'description', 'image')

#     def save(self, commit=True, user=None):
#         instance = super().save(commit=False)
#         if user:
#             instance.account = user.account
#         if commit:
#             instance.save()
#             # self.add_image_labels(instance)

#     def add_image_labels(self, image_instance):
#         api_key = 'acc_23c683b3a6a6147'
#         api_secret = 'c45920b2b1e0885dbc39958a084ee6a4'
#         # image_url = 'https://collegesdirectory.in/World/MasterAdmin/College-Master/College_Logo/Logo-1606151851.jpg'
#         image_url = self.get_absolute_url(image_instance)  # Use the request object to build the absolute URL
#         r = requests.get(image_url)
#         print("========= " + str(r.status_code))

#         time.sleep(10)
#         response = requests.get(
#             f'https://api.imagga.com/v2/tags?image_url={image_url}',
#             auth=(api_key, api_secret)
#         )

#         if response.status_code == 200:
#             labels_data = response.json().get('result', {}).get('tags', [])
#             labels = [label['tag']['en'] for label in labels_data]
#             print(labels)
#             for label_name in labels:
#                 label, _ = Label.objects.get_or_create(name=label_name)
#                 image_instance.labels.add(label)

#     def get_absolute_url(self, image_instance):
#         request = self.instance.request
#         if request:
#             return request.build_absolute_uri(image_instance.image.url)
#         return None



class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'description', 'image')

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.account = user.account
        if commit:
            instance.save()
            hosted_image_url = self.upload_to_freeimagehost(instance.image)
            print(hosted_image_url)
            if hosted_image_url:
                self.add_image_labels(instance, hosted_image_url)
        return instance

    @staticmethod
    def upload_to_freeimagehost(image_file):
        url = 'https://freeimage.host/api/1/upload'
        api_key = '6d207e02198a847aa98d0a2a901485a5'  # Replace with your actual API key
        action = 'upload'
        format = 'json'

        payload = {
            'key': api_key,
            'action': action,
            'format': format
        }

        files = {
            'source': image_file
        }

        response = requests.post(url, data=payload, files=files)

        if response.status_code == 200:
            result = response.json()
            image_url = result['image']['url']
            return image_url
        else:
            return None


    def add_image_labels(self, image_instance, image_url):
        api_key = 'x'
        api_secret = 'x'
        response = requests.get(
            f'https://api.imagga.com/v2/tags?image_url={image_url}',
            auth=(api_key, api_secret)
        )
        print(response.text)
        if response.status_code == 200:
            labels_data = response.json().get('result', {}).get('tags', [])
            labels = [label['tag']['en'] for label in labels_data]
            print(labels)
            for label_name in labels:
                label, _ = Label.objects.get_or_create(name=label_name)
                image_instance.labels.add(label)
