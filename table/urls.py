from django.urls import path
from . import views
from .views import autosuggest

urlpatterns = [
	path('', views.home, name = "home" ),
	path('fixtures/', views.fixtures, name = "fixtures"),
	path('club/<str:pk>/', views.club, name = "club"),
	path('inputscores/', views.inputScores, name = 'inputScores'),
	path('clublist/', views.clubsView, name = 'clubsView'),
	path('players/', views.playersView, name = 'players'),
	path('autosuggest/', autosuggest, name = 'autosuggest')
]