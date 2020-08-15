from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import GameServerForm

# Create your views here.
def newgameserver(request):
    form = GameServerForm()
    return render(request, 'new_game_server.html', {'form': form})


#def newgameserver(request):
#    ## check for post request
#    if request.method == 'POST':
#        form = GameServerForm(request.POST)

        #if form.is_valid():
        #    return HttpResponseRedirect('/success')

#    else:
#        form = GameServerForm()

#    return render(request, 'new_game_server.html', {'form': form})
