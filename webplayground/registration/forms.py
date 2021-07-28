from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Campo obligatorio, 254 caracteres como maximo que debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def cleam_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "El email ya fue registrado, usa otro :p")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control-file mt-3', 'rows': 3, 'placeholder': 'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control-file mt-3', 'placeholder': 'Enlace'}),
        }
