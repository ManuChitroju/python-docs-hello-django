from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
   return HttpResponse("Hello....How are you")

#def hello(request):
#   return render(request, 'personal/first.html')
