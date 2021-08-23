from django import	forms
from django.contrib.auth.forms import UserCreationForm,	UserChangeForm
from django.contrib.auth.models import User
from .models import ResultHistory
#this is the custom user form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= User
        fields= ['username', 'first_name', 'last_name']
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=User
        fields=UserChangeForm.Meta.fields
class ResultForm(forms.ModelForm):
    class Meta:
        model = ResultHistory
        fields = ['expression', 'result']

#lets create custom form for posting result data
