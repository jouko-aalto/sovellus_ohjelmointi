from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Boardgame
from .forms import BoardgameForm
from django.http import Http404

# Create your views here.

def index(request):
    #Home page
    return render(request, "board_game_app/index.html")

@login_required
def board_games(request):
    #shows all games
    board_games = Boardgame.objects.filter(owner=request.user).order_by("date_added")
    context = {"board_games" : board_games}
    return render(request, "board_game_app/board_games.html", context)

@login_required
def board_game(request, board_game_id):
    #shows a games
    board_game = Boardgame.objects.get(id=board_game_id)
    #make sure the topic belongs to the user
    if board_game.owner != request.user:
        raise Http404
    context = {"board_game" : board_game}
    return render(request, "board_game_app/board_game.html", context)
    
@login_required
def new_board_game(request):
    #adds new board_game to site
    if request.method != "POST":
        form = BoardgameForm()
    else:
        form = BoardgameForm(data=request.POST)
        if form.is_valid():
            new_board_game = form.save(commit=False)
            new_board_game.owner = request.user
            new_board_game.save()
            return redirect("board_game_app:board_games")
    context = {"form": form}
    return render(request, "board_game_app/new_board_game.html", context)

@login_required
def edit_board_game(request, board_game_id):
    board_game = Boardgame.objects.get(id=board_game_id)

    if board_game.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = BoardgameForm(instance=board_game)
    else:
        form = BoardgameForm(instance=board_game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("board_game_app:board_game", board_game_id=board_game.id)

    context = {"board_game":board_game, "form":form}
    return render(request, "board_game_app/edit_board_game.html", context)