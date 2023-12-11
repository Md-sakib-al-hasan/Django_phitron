from  django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels= {
            'name': 'student_name',
            'roll': 'student_roll',
        }