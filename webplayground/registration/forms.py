from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWhitEmail(UserCreationForm):
     email = forms.EmailField(required=True, help_text="Campo obligatorio, 254 caracteres como maximo que debe ser valido")

     class Meta:
          model = User
          fields = ("username", "email", "password1", "password2")
          
     def cleam_email(self)
          email = self.cleaned_data.get("email")
          if User.objects.filter(email=email).exists():
               raise forms.ValidationError("El email ya fue registrado, usa otro :p")
          return email
