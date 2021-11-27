from django.urls import path
from . import views

urlpatterns = [
    
    path('helpdesk', views.helpdesk,name='helpdesk'),
    
]