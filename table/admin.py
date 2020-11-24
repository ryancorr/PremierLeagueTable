from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(Club)
admin.site.register(Game)
admin.site.register(Player)