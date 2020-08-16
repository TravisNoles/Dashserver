from django import forms
from .models import Game


class GameServerForm(forms.Form):
    name = forms.CharField(label='Game Server Name: ', max_length=50)

    gametype = forms.ChoiceField(choices=[
        ('terraria', 'Terraria'),
        ('minecraft', 'Minecraft')
        ])

    class Meta:
        model = Game
        fields = ('name', 'gametype')


