from django.http import HttpResponse

def hello():
    return HttpResponse('<h1>Hello</h1>')