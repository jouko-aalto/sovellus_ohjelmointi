from django import forms
from .models import Boardgame, Review

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ["name", "designer", "artist", "publisher", "year_published"]
        labels = {"name": "Board games name", "designer": "Designer", "artist": "Artist", "publisher": "Publisher", "year_published": "Year published" }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["my_review", "stars", "unfinished"]
        labels = {"my_review":"Review:", "stars":"Stars:", "unfinished":"Have you not played the game?"}
        widget = {"my_review" : forms.Textarea(attrs={"cols":80})}