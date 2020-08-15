from django import forms


class GameServerForm(forms.Form):
    name = forms.CharField()
    type = forms.ChoiceField(choices=[
        ('terraria', 'Terraria'),
        ('minecraft', 'Minecraft')
        ])


    gameserver = forms.CharField(label='Game Server', max_length=20)


