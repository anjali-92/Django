from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tictactoe.models import Game,Invitation
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

'''
@login_required
def home(request):
    return render(request,'users/home.html')
'''

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = active_games.filter(next_to_move=request.user)
    other_games = active_games.exclude(next_to_move=request.user)
    #getting invitations by using related name of field
    invitations = request.user.invitation_received.all()
    context = { 
	    'other_games':other_games , 
	    'waiting_games':waiting_games , 
	    'finished_games':finished_games,
	    'invitations':invitations
	    }

    return render(request, "users/home.html", context)

class SignUp(CreateView):
    form_class = UserCreationForm 
    template_name = "users/signup.html"
    success_url = reverse_lazy("users_home")
