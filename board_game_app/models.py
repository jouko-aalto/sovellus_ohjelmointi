from django.db import models
from django.contrib.auth.models import User



class Boardgame(models.Model): #creating the class
    #createing the variable with specific value types
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)     
    designer = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year_published = models.IntegerField()                               
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        #returns the books information
        return (self.name)