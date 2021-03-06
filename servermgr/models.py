from django.db import models
from vultr import Vultr, VultrError
import json

# Create your models here.
# shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Server(models.Model):
    id = models.AutoField(primary_key = True)
    hostname = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50)

    vultr_regions = [
        (2, 'Chicago'),
        (6, 'Atlanta'),
        (1, 'New Jersey'),
        (3, 'Dallas'),
        (5, 'Los Angeles'),
        (39, 'Miami'),
        (4, 'Seattle'),
        (8, 'London'),
        (22, 'Toronto'),
        (19, 'Sydney'),
        (34, 'Seoul'),
        (24, 'Paris'),
        (12, 'Silicon Valley'),
        (40, 'Singapore'),
        (7, 'Amsterdam'),
        (25, 'Tokyo'),
        (9, 'Frankfurt'),
    ]

    location = models.CharField(max_length=20, choices=vultr_regions)


    os = [
        (167, 'CentOS7'),
    ]

    operatingsystem = models.CharField(max_length=10, choices=os, default=167)

    plan = [
        (400, '1G RAM 25GB 1TB BW'),
    ]

    plan = models.CharField(max_length=40, choices=plan, default=400)

class Game(models.Model):
    name = models.CharField(max_length=50, primary_key= True)
    port = models.IntegerField(max_length=5, default=0) # autogenerated

    game_list = [
        ('terraria', 'Terraria'),
        ('minecraft', 'Minecraft'),
    ]

    gametype = models.CharField(max_length=50, choices=game_list)

    def __str__(self):
        return self.name

