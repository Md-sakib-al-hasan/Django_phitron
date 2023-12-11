from django.http import HttpResponse
def about(response):
    return HttpResponse("this is about section")

def contact(response):
    return HttpResponse("Contact with us")
def  Home(response):
    return HttpResponse("This is Home page")