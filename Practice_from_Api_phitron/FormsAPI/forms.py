<<<<<<< HEAD
from django import forms
import datetime
from FormsAPI.models import movies
from django.urls import path

class LoginForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget = forms.Textarea())
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    agree = forms.BooleanField(label="Agree")
    date = forms.DateField()
    dates =forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    choice_year = ['198','201','202']
    datechoce = forms.DateField(widget  = forms.
    SelectDateWidget())
    value = forms.DecimalField()
    email_requir = forms.EmailField(required= False,max_length=10,label='Please enter your email address',initial='Enter your email address')
    Chackbox = forms.BooleanField(initial = True)
    Day = forms.DateField(initial = datetime.date.today)
    Favorite_color = [('r','red'),('g','green'),('b','blue')]
    favorite_color = forms.ChoiceField(widget =forms.RadioSelect,choices=Favorite_color   )
    favorite_color_ = forms.ChoiceField(choices=Favorite_color   )
    Multible_choice =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Favorite_color)


    ModelMUliplechoices =forms.ModelChoiceField(
        # widget=  forms.RadioSelect,
        queryset = movies.objects.all(),
        initial=0
    )

    
    ModelMUliplechoicescheboks =forms.ModelChoiceField(
        widget= forms.CheckboxSelectMultiple,
        queryset = movies.objects.all(),
        initial=0
    )


    # file input

    field_name = forms.FileField()
    geeks_Field = forms.TypedChoiceField(choices= Favorite_color)
    dateTimeField =  forms.DateTimeField()
    durationField = forms.DurationField()
    image = forms.ImageField()
    Int = forms.IntegerField(required=False)
    ip = forms.GenericIPAddressField()
    null = forms.NullBooleanField()
    ReField = forms.RegexField(regex='[0-9]')

    name = forms.CharField(
                error_messages={
               'sk': 'Please enter your name'
=======
from django import forms
import datetime
from FormsAPI.models import movies
from django.urls import path

class LoginForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget = forms.Textarea())
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    agree = forms.BooleanField(label="Agree")
    date = forms.DateField()
    dates =forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    choice_year = ['198','201','202']
    datechoce = forms.DateField(widget  = forms.
    SelectDateWidget())
    value = forms.DecimalField()
    email_requir = forms.EmailField(required= False,max_length=10,label='Please enter your email address',initial='Enter your email address')
    Chackbox = forms.BooleanField(initial = True)
    Day = forms.DateField(initial = datetime.date.today)
    Favorite_color = [('r','red'),('g','green'),('b','blue')]
    favorite_color = forms.ChoiceField(widget =forms.RadioSelect,choices=Favorite_color   )
    favorite_color_ = forms.ChoiceField(choices=Favorite_color   )
    Multible_choice =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Favorite_color)


    ModelMUliplechoices =forms.ModelChoiceField(
        # widget=  forms.RadioSelect,
        queryset = movies.objects.all(),
        initial=0
    )

    
    ModelMUliplechoicescheboks =forms.ModelChoiceField(
        widget= forms.CheckboxSelectMultiple,
        queryset = movies.objects.all(),
        initial=0
    )


    # file input

    field_name = forms.FileField()
    geeks_Field = forms.TypedChoiceField(choices= Favorite_color)
    dateTimeField =  forms.DateTimeField()
    durationField = forms.DurationField()
    image = forms.ImageField()
    Int = forms.IntegerField(required=False)
    ip = forms.GenericIPAddressField()
    null = forms.NullBooleanField()
    ReField = forms.RegexField(regex='[0-9]')

    name = forms.CharField(
                error_messages={
               'sk': 'Please enter your name'
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
                })