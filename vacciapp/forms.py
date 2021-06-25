from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    # name =  forms.CharField(max_length=100)
    # phone = forms.CharField(max_length=100)
    # aadhar = forms.CharField(max_length=100)
    # age = forms.CharField(max_length=100)
    # gender = forms.CharField(max_length=100)
    # address = forms.CharField(max_length=100)
    # city = forms.CharField(max_length=100)
    # state = forms.CharField(max_length=100)
    # pincode = forms.CharField(max_length=100)
    # vtaken = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # 'name',,'phone','aadhar','age','gender','address','city','state','pincode','vtaken'

class PassChangeForm(PasswordChangeForm):
    pass

