from django.contrib import admin

# Register your models here.
from .models import Track, Genre
admin.site.register(Track)
admin.site.register(Genre)
