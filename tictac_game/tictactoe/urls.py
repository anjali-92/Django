from django.conf.urls import patterns, include, url
from .views import  AllGamesList

urlpatterns = patterns('tictactoe.views',
	url(r'^invite$','new_invitation',name='tictactoe_invite'),
	url(r'^accept_invite/(?P<pk>[0-9]+)/$','accept_invitation',name='tictactoe_invite_accept'),
        url(r'^game/(?P<pk>\d+)/$','game_detail',name='tictactoe_game_detail'),
	url(r'^game/(?P<pk>\d+)/do_move$','do_move',name="tictactoe_do_move"),
	url(r'^game/all',AllGamesList.as_view()),
	)
