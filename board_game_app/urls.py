from django.urls import path
from . import views

app_name = 'board_game_app'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all board games
    path("board_games/<int:toggle>", views.board_games, name="board_games"),
    #Individual board game page
    path("board_game/<int:board_game_id>/", views.board_game, name="board_game"),
    #Page for adding new board games 
    path('new_board_game/', views.new_board_game, name='new_board_game'),
    #Edit
    path("edit_board_game/<int:board_game_id>/", views.edit_board_game, name="edit_board_game"),
    #Borrow
    path("borrow_board_game/<int:board_game_id>/", views.borrow_board_game, name="borrow_board_game"),
    #Return
    path("return_board_game/<int:board_game_id>/", views.return_board_game, name="return_board_game"),
    #Review
    path("review/", views.reviews, name="reviews"),
    #New reviews
    path("new_review/<int:board_game_id>/", views.new_review, name="new_review"),
    #Adding review
    path("edit_review/<int:review_id/", views.edit_review, name="edit_review"),
]