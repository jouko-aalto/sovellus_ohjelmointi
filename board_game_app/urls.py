from django.urls import path
from . import views

app_name = 'bord_game_app'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all board games
    path("books/", views.board_games, name="board_games"),
    #Individual board game page
    path("book/<int:book_id>/", views.board_game, name="board_game"),
    #Page for adding new board games 
    path('new_book/', views.new_board_game, name='new_board_game'),
]