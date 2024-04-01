from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
	def __init__(self, *args, **kargs):
		super().__init__(*args, **kargs)
		self.fields["username"].widget.attrs.update({
			'require': '',
			'name' : 'username',
			'minlength' : '3',
			'maxlength' : '150',
			'autofocus' : '',
			'id':'id_username',
			'placeholder' : 'Username',
		})
		self.fields["password1"].widget.attrs.update({
			'require': '',
			'name' : 'password1',
			'id':'id_password1',
			'placeholder' : 'Password',
		})
		self.fields["password2"].widget.attrs.update({
			'require': '',
			'name' : 'password2',
			'id':'id_password2',
			'placeholder' : 'Retype password',
		})
	class Meta:
		model = get_user_model()
		fields = ['username', 'password1', 'password2']	#field to be included in the form

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def __init__(self, *args, **kargs):
		super().__init__(*args, **kargs)
		self.fields["username"].widget.attrs.update({
			'require': '',
			'name' : 'username',
			'minlength' : '3',
			'maxlength' : '150',
			'autofocus' : '',
			'id':'id_username',
			'placeholder' : 'Username',
		})
		self.fields["password"].widget.attrs.update({
			'require': '',
			'name' : 'password',
			'id':'id_password',
			'placeholder' : 'Password',
		})
