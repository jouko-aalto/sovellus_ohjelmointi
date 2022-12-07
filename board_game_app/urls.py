from django.urls import path
from . import views

app_name = 'board_game_app'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all board games
    path("board_games/", views.board_games, name="board_games"),
    #Individual board game page
    path("board_game/<int:board_game_id>/", views.board_game, name="board_game"),
    #Page for adding new board games 
    path('new_board_game/', views.new_board_game, name='new_board_game'),
    #Edit
    path("edit_board_game/<int:board_game_id>/", views.edit_board_game, name="edit_board_game"),
]