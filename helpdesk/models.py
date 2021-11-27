from django.db import models

# Create your models here.



class Ticket(models.Model):

    title =models.CharField(max_length=50)
    summary = models.CharField(max_length=150)
    Description = models.CharField(max_length=150)
    source = models.CharField(max_length=99,default="")
    target = models.CharField(max_length=99,default="")

    def __str__(self):
        return self.title

    


