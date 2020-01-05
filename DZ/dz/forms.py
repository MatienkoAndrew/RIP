from django import forms
from .models import Service
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class PostForm(forms.ModelForm):

	class Meta:
		model = Service
		fields = ('author', 'title', 'text', 'price', 'image')

class LoginForm(AuthenticationForm):
	pass

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=30, label="Почта")
	first_name = forms.CharField(max_length=30, label="Имя")
	last_name = forms.CharField(max_length=30, label="Фамилия")

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = ''
		self.fields['password1'].help_text = ''

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email',)


class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')