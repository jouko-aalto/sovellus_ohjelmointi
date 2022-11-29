from django import forms
from .models import Boardgame

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ["name", "designer", "artist", "publisher", "year_published"]
        labels = {"name": "Board games name", "designer": "Designer", "artist": "Artist", "publisher": "Publisher", "year_published": "Year published" }