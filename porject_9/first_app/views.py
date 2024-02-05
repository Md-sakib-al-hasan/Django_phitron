from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def  home(request):
    response = render(request, 'home.html')
    # response.set_cookie('name','rahim',max_age=10)
    response.set_cookie('name','rahim', expires=datetime.utcnow()+timedelta(days=7))
    return response 

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render (request, 'get_cookies.html',{'name':name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

def session_add(request):
    # data = {
    #     'name': 'rahim',
    #     'age': 23,
    #     'language': 'Bangla'

    # }
   
    # request.session.update(data)
    request.session['name'] = 'sakib'
    return render(request, 'home.html')
def session_get(request):
    if 'name' in request.session:
         
        data = request.session
        request.session.modified = True
        return render(request,'get_session.html',{'data':data})
    else:
        return HttpResponse("your set has been ex")

def session_delete(request):
    request.session.flush()
    return render(request,'delete_cookie.html')