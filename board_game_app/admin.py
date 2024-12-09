from django.contrib import admin
from .models import Boardgame, Review

admin.site.register(Boardgame)
admin.site.register(Review)
admin.site.site_header = "Board Game Madness"