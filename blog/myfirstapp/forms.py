from django import forms
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']



#create form
class myform(forms.ModelForm):
    class Meta:                                             #fields can be insert in the form of list
        model=info                                          #model=table_name
        fields='__all__'
        #('firstname','lastname','email')            #fields=no. of fields of form  (min these two must be defined)




#form for posting comment
class blogform(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(
        attrs={
                'class':'form-control',
                'placeholder':'Title of Post'
                
            }
        ))
    description=forms.CharField(widget=forms.Textarea(
        attrs={
                'class':'form-control txt_input',
                'placeholder':'Whats on your mind...?',
                'rows':'3',
                'border': '0px none'
            }
        ))
    image=forms.FileField()
    class Meta:
        model=blog
        fields=('title','description','image')

