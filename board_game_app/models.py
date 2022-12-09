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

class Review(models.Model): #creating the class
    #createing the variable with specific value types
    my_review = models.CharField(max_length=200)       
    stars = models.IntegerField()
    unfinished = models.BooleanField()
    #automaticly updates date when book is made           
    date_added = models.DateTimeField(auto_now_add=True)
    #automaticly updates date when book is made or modified  
    date_modified  = models.DateTimeField(auto_now=True)
    #Foreing key refers to another model called "book"
    reviewed_book = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        #returns the books information
        return (self.my_review) 