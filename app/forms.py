from django import forms
user=[('male','MALE'),('female','FEMALE')]
class SingUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=user)
    gender=forms.ChoiceField(choices=user,widget=forms.RadioSelect)
    