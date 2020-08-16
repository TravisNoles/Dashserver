from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import GameServerForm

# Create your views here.
def newgameserver(request):

    if request.method == 'POST':
        form = GameServerForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            gametype = form.cleaned_data['gametype']
            print(name,gametype)
            print('VALID')

        else:
            form = GameServerForm()

    form = GameServerForm()
    return render(request, 'forms/new_game_server.html', {'form': form})
