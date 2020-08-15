from django import forms


class GameServerForm(forms.Form):
    name = forms.CharField(label='Game Server Name: ', max_length=50)

    type = forms.ChoiceField(choices=[
        ('terraria', 'Terraria'),
        ('minecraft', 'Minecraft')
        ])




