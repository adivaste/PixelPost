from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from main.models import Image, Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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

    


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'description', 'image')

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.account = get_user_model().objects.get(id=user.id).account
        if commit:
            instance.save()

