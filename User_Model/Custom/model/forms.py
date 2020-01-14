from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import Info


class InfoCreationForm(UserCreationForm):
    class Meta:
        model = Info
        fields = ('username','email',)

class InfoChangeForm(UserChangeForm):
    class Meta:
        model = Info
        fields = ('username','email',)
