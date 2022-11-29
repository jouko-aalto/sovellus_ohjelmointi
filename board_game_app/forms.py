from django import forms
from .models import Boardgame

class Boardgame(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ["name", "designer", "artist", "publisher", "year_published"]
        labels = {"name": "Books name", "designer": "Designer", "artist": "Artist", "publisher": "Publisher", "year_published": "Year published" }