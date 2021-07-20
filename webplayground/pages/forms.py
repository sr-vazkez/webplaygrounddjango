from django import forms
from django.forms import widgets

from .models import Page

class PageForm(forms.ModelForm):

     class Meta:
          model = Page
          fields = ['title','content','order']
          widgets = {
          'title': forms.TextInput(attrs={'class':'form-control'}),
          'content': forms.TextArea(attrs={'class':'form-control'}),
          'order': forms.TextNumber(attrs={'class':'form-control'}),
          }