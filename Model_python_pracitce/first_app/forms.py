from django import forms
from first_app.models import  MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
