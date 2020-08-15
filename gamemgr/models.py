from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    games_list = [
        (0, 'Terraria'),
        (1, 'Minecraft'),
    ]

    gameserver = models.CharField(max_length=20, choice=games_list)