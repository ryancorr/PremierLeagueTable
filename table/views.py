from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import *
from .forms import *
import datetime

# Create your views here.

def home(request):

	teams = Team.objects.all().order_by('-points','-gd','-gf')
	count = 1
	for team in teams:
		team.position = count
		count += 1
		team.save()
	startDate = datetime.date.today() -  datetime.timedelta(days = 3 )
	playing = Game.objects.filter(gamedate__range = [startDate, datetime.date.today()]).order_by('-gamedate')[:6]

	return render(request, 'table/home.html', {'teams': teams, 'playing': playing})

def fixtures(request):
	numWeeks = 1
	games = getFixtures(numWeeks,0)
	playingDates = games[0]
	idDict = games[1]

	return render(request, 'table/games.html', {'playingDates': playingDates, 'idDict' : idDict})

def club(request, pk):
	club = Club.objects.get(id = pk)
	team = Team.objects.get(id = pk)
	gk = Player.objects.filter(club_id = pk, position = 'GK').order_by('number')
	df = Player.objects.filter(club_id = pk, position = 'DF').order_by('number')
	mf = Player.objects.filter(club_id = pk, position = 'MF').order_by('number')
	fw = Player.objects.filter(club_id = pk, position = 'FW').order_by('number')
	flags = {"England": "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/100px-Flag_of_England.svg.png" , 
	"Wales" : "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Wales_%281959%E2%80%93present%29.svg/100px-Flag_of_Wales_%281959%E2%80%93present%29.svg.png" , 
	"Scotland": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Flag_of_Scotland.svg/100px-Flag_of_Scotland.svg.png" , 
	"Northern Ireland": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Ulster_Banner.svg/100px-Ulster_Banner.svg.png"}

	return render(request, 'table/club.html', {'club': club, 'team': team, 'gk' : gk, 'df': df, 'mf': mf, "fw": fw, 'flags': flags})



def clubsView(request):
	teams = Team.objects.all().order_by("name")

	return render(request, 'table/clubList.html', {'teams': teams})



def inputScores(request):
	startDate = datetime.date.today() -  datetime.timedelta(days = 5)
	endDate = datetime.date.today()
	today = Game.objects.filter(gamedate__range = [startDate, endDate])

	if today.exists():
		GameFormSet = modelformset_factory(Game, fields= ('teamone','teamtwo', 'teamonegoals', 'teamtwogoals', 'gamedate'), extra = 0)
		if request.method == 'POST':
			formset = GameFormSet(request.POST, queryset = today)
			if formset.is_valid():
				formset.save()
				return redirect('/')
		else:	
			formset = GameFormSet(queryset = today)

		updateTable(startDate,endDate)
		return render(request, 'table/inputscores.html', {'formset' : formset})
	else:
		return HttpResponse("<h1> No Games To Input Today <h1>")

def updateTable(startDate,endDate):
	updates = Game.objects.filter(gamedate__range = [startDate, endDate])

	for game in updates:	
		one = Team.objects.get(id = game.teamone.id)
		two = Team.objects.get(id = game.teamtwo.id)
		one.played = one.played + 1
		two.played = two.played + 1
		one.gf = one.gf + game.teamonegoals
		one.ga = one.ga + game.teamtwogoals
		one.gd = one.gd + game.teamonegoals - game.teamtwogoals
		two.gf = two.gf + game.teamtwogoals
		two.ga = two.ga + game.teamonegoals
		two.gd = two.gd + game.teamtwogoals - game.teamonegoals


		if int(game.teamonegoals) > int(game.teamtwogoals):
			one.won = one.won + 1
			two.lost = two.lost + 1
			one.points = one.points + 3
			one.curForm = "W" + one.curForm[:-1]
			two.curForm = "L" + two.curForm[:-1]
		elif int(game.teamtwogoals) > int(game.teamonegoals):
			two.won = two.won + 1
			one.lost = one.lost + 1
			two.points = two.points + 3
			one.curForm = "L" + one.curForm[:-1]
			two.curForm = "W" + two.curForm[:-1]
		else: 
			one.drawn = one.drawn + 1
			two.drawn = two.drawn + 1
			one.points = one.points + 1
			two.points = two.points + 1
			one.curForm = "D" + one.curForm[:-1]
			two.curForm = "D" + two.curForm[:-1]
		one.save()
		two.save()


def getFixtures(numWeeks,prevDays):
	startDate = datetime.date.today() -  datetime.timedelta(days = prevDays )
	endDate = startDate + datetime.timedelta(days = 6 * numWeeks)
	playing = Game.objects.filter(gamedate__range = [startDate,endDate]).order_by('gamedate')
	playingDates = {}
	itrDate = playing.first().gamedate

	curList = []
	count = 0
	for item in playing:
		if item.gamedate == itrDate:
			curList.append(item)
		else:
			playingDates[itrDate] = curList
			curList = []
			itrDate = item.gamedate
			curList.append(item)
	playingDates[itrDate] = curList


	idDict = {}
	for item in playing:
		key = item.id
		idDict.setdefault(key, [])
		idDict[item.id].append(item.teamone_id)
		idDict[item.id].append(item.teamtwo_id)
	return [playingDates, idDict]