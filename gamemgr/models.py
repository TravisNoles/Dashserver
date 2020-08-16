from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    games_list = [
        (0, 'Terraria'),
        (1, 'Minecraft'),
    ]

    class Meta:
        abstract = True
        app_label = 'dashserver'

    gametype = models.CharField(max_length=20, choices=games_list)