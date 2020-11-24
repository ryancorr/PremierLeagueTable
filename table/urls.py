from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name = "home" ),
	path('club/<str:pk>/', views.club, name = "club"),
	path('inputscores/', views.inputScores, name = 'inputScores')
]