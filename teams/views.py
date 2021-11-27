from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def teams(request):
    #now = datetime.datetime.now()
    html = "<html><body>Teams Page%s.</body></html>"
    return HttpResponse(html)
