from django import forms
from django.core import validators

# class contactForm(forms.Form):
#     name = forms.CharField(label="Full Name : ", initial="Rahime", help_text="please provide your full name",required=False, disabled=True,widget = forms.Textarea(attrs={'id':'llllllll','class':'class1 class2'}))
    # email = forms.EmailField(label="email")
    # file = forms.FileField()
    # age = forms.IntegerField(label="age")
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birday = forms.DateField()
    # application = forms.DateTimeField()
    # CHOICE=[('s','small'),('m','medium'),('l','long')]
    # size =  forms.ChoiceField(choices=CHOICE)
    # meal = [('s','spice'),('sw','switely'),('l','lemon')]
    # pixx = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#     name = forms.CharField(widget = forms.TextInput)
#     email = forms.CharField(widget= forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a valid name")
    
    # def clean_email(self):
    #     valeamil = self.cleaned_data['email']
    #     if  '.ocm' not in valeamil:
    #         raise forms.ValidationError("please enter .com")
    #     return valeamil

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a valid name")
    #     if  '.ocm' not in  valemail:
    #         raise forms.ValidationError("please enter .com")


class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10,message="enter ysr athe")] )
    email = forms.CharField(validators=[validators.EmailValidator(message="sk")])
    age =forms.CharField()   
        
    
class passwrodValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        if val_pass != val_conpass:
            raise forms.ValidationError("password must")