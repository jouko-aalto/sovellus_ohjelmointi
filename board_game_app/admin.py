from django.contrib import admin
from .models import Boardgame

admin.site.register(Boardgame)
admin.site.site_header = "Board Game Madness"