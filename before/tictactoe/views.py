from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404 , redirect

from .forms import InvitationForm, MoveForm
from .models import Invitation, Game, Move
from django.core.exceptions import PermissionDenied

from django.views.generic import ListView

class AllGamesList(ListView):
    model = Game

@login_required
def new_invitation(request):
    if request.method == 'POST':
	invitation = Invitation(from_user=request.user)
	form = InvitationForm(data = request.POST,instance = invitation)
	if form.is_valid():
	    form.save()
	    return redirect('users_home')
    else:
        form = InvitationForm()
    return render(request, "tictactoe/new_invitation.html",{'form':form})

@login_required
def accept_invitation(request, pk):
    #get object of invitation class having pk primary key
    invitation = get_object_or_404(Invitation, pk=pk)
    if not request.user == invitation.to_user:
	raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
	    game = Game.objects.add_new(invitation)
	    invitation.delete()
	    return redirect(game.get_absolute_url())
	else:
	    invitation.delete()
	    return redirect('users_home')
    else:
        return render(request, 'tictactoe/accept_invitation.html',{'invitation':invitation})

@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if game.is_users_move(request.user):
	return redirect('tictactoe_do_move', pk=pk)
    else:
        return render(request, "tictactoe/game_detail.html",{'game':game})

    print "game_detail unreached place"
    return redirect('users_home')

@login_required
def do_move(request, pk):
    #import ipdb
    #ipdb.set_trace()

    game = get_object_or_404(Game, pk=pk)
    if not game.is_users_move(request.user):
	raise PermissionDenied 
    context = { 'game': game }
    if request.method == 'POST':
	form = MoveForm(data=request.POST, instance=game.create_move() )
        print "IN POST do_move"
	context['form'] = form
	if form.is_valid():
            move = form.save()
            game.update_after_move(move)
            game.save()
	    return redirect('tictactoe_game_detail', pk = pk)
    else:
	context['form'] = MoveForm()
    return render(request,"tictactoe/game_do_move.html", context )
