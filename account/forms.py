from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

from django import forms

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'block w-full rounded-md border-0 px-2 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'})
        
        # Mark  email field as required
        
        self.fields['email'].required = True
        
    # Email Validation
    
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('This email is invalid')
        
        if len(email) >= 350:
            
            raise forms.ValidationError("Your email is too long")
        
        return email
    
    
class UpdateUserForm(forms.ModelForm):
    
    password = None
    
    class Meta:
        
        model = User 
        
        fields = ['username', 'email']
        exclude = ['passwoerd1', 'passwoerd2']
        
        
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'w-full flex-shrink appearance-none border-gray-300 bg-white py-2 px-4 text-base text-gray-700 placeholder-gray-400 focus:outline-none'})
            
            
        self.fields['email'].required = True
        
        
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            
            raise forms.ValidationError('This email has already been used')
        
        if len(email) >= 350:
            
            raise forms.ValidationError("Your email is too long")
        
        return email
    

    
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'block w-full rounded-md border-0 px-2 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'})