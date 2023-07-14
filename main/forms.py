from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from main.models import Image, Account, Label
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import requests

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
            self.add_image_labels(instance)
    
    def add_image_labels(self, image_instance):
        api_key = 'acc_23c683b3a6a6147'
        api_secret = 'c45920b2b1e0885dbc39958a084ee6a4'
        image_url = 'https://collegesdirectory.in/World/MasterAdmin/College-Master/College_Logo/Logo-1606151851.jpg'
        # print(image_instance.image.url)

        response = requests.get(
            f'https://api.imagga.com/v2/tags?image_url={image_url}',
            auth=(api_key, api_secret)
        )

        if response.status_code == 200:
            labels_data = response.json().get('result', {}).get('tags', [])
            labels = [label['tag']['en'] for label in labels_data]
            print(labels)
            # image_instance.labels.add(*labels)
            # image_instance.labels.set(labels)
            for label_name in labels:
                label, _ = Label.objects.get_or_create(name=label_name)
                image_instance.labels.add(label)


