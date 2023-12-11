from django import  forms
from first_app.models import LoginModel

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'