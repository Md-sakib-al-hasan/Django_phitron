from django.shortcuts import render
# from .forms import contactForm
from .forms import StudentData as ps

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    name= request.POST.get('username','sakib')
    email= request.POST.get('email','eamil')
    select= request.POST.get('select','null')
    return render(request, 'about.html',{'name':name, 'email':email,'select':select})

def form(request):
    return render(request, 'form.html')

def  DjangoForm (request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/'+file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request,'django_form.html',{'form':form})
    else:
        form = contactForm()
    return render(request,'django_form.html',{'form':form})


def passwordvalidation(request):
    
    if request.method == 'POST':
        form = ps(request.POST)
        
        if form.is_valid():
            print("sk")
            print(form.cleaned_data)
    else:
        form = ps()
    return render(request,'django_form.html',{'form':form})

  
def passw(request):

    if request.method == 'POST':
        form = StudentData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = StudentData()
    else:
        form = StudentData()
    return render(request,'django_form.html',{'form':form})