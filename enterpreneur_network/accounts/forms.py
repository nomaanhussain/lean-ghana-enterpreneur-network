from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from allauth.account.forms import SignupForm 
from django import forms
  
class CustomSignupForm(SignupForm): 
    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user): 
     	user.first_name = self.cleaned_data['first_name'] 
     	user.last_name = self.cleaned_data['last_name'] 
     	user.save() 
     	return user 
# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#         # fields = ['username','first_name','last_name','email','password1','password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


