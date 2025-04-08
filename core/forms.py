from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Answer, Question

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']