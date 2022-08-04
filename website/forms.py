from django.forms import EmailInput, ModelForm, TextInput, PasswordInput

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'Name': TextInput(attrs={"type": "text"}),
            'Email': EmailInput(attrs={"type": "email"}),
            'Password': PasswordInput(attrs={"type": "password"})
        }
