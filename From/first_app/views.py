from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def home (request):
    if request.method == 'POST':
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/'+file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
                    
                    
    else:
        form = LoginForm(request.POST)
    return render(request, './first_app/django_from.html',{'form':form})