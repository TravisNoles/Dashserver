from django.contrib import admin
from servermgr.models import Server
from .models import Game

# Register your models here.

admin.site.register(Server)
admin.site.register(Game)