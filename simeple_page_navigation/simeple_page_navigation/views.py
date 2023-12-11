from django.shortcuts import render
import datetime
def home(request):
    sk = "<P>kamal khan never day</p>"
    return render(request,'home.html',{'sk':sk})