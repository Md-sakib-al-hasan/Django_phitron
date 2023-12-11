from django.shortcuts import render
import datetime

# Create your views here.
def home (request):
    person = {"birth": datetime.datetime.now(), "author":"sakib","age":21,'List':['python', 'is', 'fun'],
              "courses":[{'id': 1,'name':'python','fee':5000},
                         {'id': 2,'name':'html','fee':100},
                         {'id': 3,'name':'css','fee':9000}]}
    return render(request, 'index.html',person)
