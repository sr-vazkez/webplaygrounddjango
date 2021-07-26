from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
# Create your views here.


class SignUpView(CreateView):
  form_class = UserCreationFormWithEmail
  template_name = 'registration/signup.html'

  def get_success_url(self):
    return reverse_lazy('login') + '?register'

  def get_form(self, form_class=None):
    form = super(SingUpView, self).get_form()
    #modificar en tiempo real
    form.fields['username'].widget = forms.TextInput(attr={'class:'form-control mb-2', 'placeholder':'Nombre de Usuario'})
    form.fields['email'].widget = forms.EmailInput(attr={'class:'form-control mb-2', 'placeholder':'Correo Electronico'})
    form.fields['password1'].widget = forms.PasswordInput(attr={'class:'form-control mb-2', 'placeholder':'Password '})
    form.fields['password2'].widget = forms.PasswordInput(attr={'class:'form-control mb-2', 'placeholder':'Repite tu password'})
    return form  
  