#from django.http import HttpResponse


#def index(request):
#    return HttpResponse('usefulsite -- Hello, world! -- ¯\(°:°)/¯')
from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html') # Используйте render
