from django.shortcuts import render
from django.http import HttpResponse
from . models import Ticket
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def helpdesk(request):
        username = request.user.username
        email = request.user.email
    
        if email.endswith("@yahoo.com"):
            source = "YAHOO"
            target = "YAHOO"
            ticket = Ticket.objects.filter(Q(source=source)|Q(target=target)).values()
            return render(request,'user_data/helpdesk.html',
            {
                'ticket' : ticket
            })
            
        elif email.endswith("@gmail.com"):
            source = "GMAIL"
            target = "GMAIL"
            ticket = Ticket.objects.filter(Q(source=source)|Q(target=target)).values()
            return render(request,'user_data/helpdesk.html',
            {
                'ticket' : ticket
            }
            )
        elif email.endswith("@bankbuddy.com"):
            source = "BANKBUDDY"
            target = "BANKBUDDY"
            ticket = Ticket.objects.filter(Q(source=source)|Q(target=target)).values()
            return render(request,'user_data/helpdesk.html',
            {
                'ticket' : ticket
            }
            )
