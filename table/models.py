from django.db import models

# Create your models here.


class Team(models.Model):
	position = models.IntegerField(null = True)
	name = models.CharField(max_length = 200, null = True)
	played = models.IntegerField()
	won = models.IntegerField()
	drawn = models.IntegerField()
	lost = models.IntegerField()
	gf = models.IntegerField()
	ga = models.IntegerField()
	gd = models.IntegerField()
	points = models.IntegerField()
	curForm = models.CharField(max_length = 200, null = True)
	

	def __str__(self):
		return self.name

class Club(models.Model):
	team = models.ForeignKey(Team, on_delete = models.CASCADE, null = True)
	stadium = models.CharField(max_length = 50, null = True)
	nickname = models.CharField(max_length = 50, null = True)
	color = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.team.name


class Game(models.Model):
	teamone = models.ForeignKey(Team, on_delete = models.SET_NULL, null = True, related_name = 'teamone')
	teamtwo = models.ForeignKey(Team, on_delete = models.SET_NULL, null = True, related_name = 'teamtwo')
	teamonegoals = models.IntegerField(null = True)
	teamtwogoals = models.IntegerField(null = True)
	gamedate = models.DateField(null = True)

	def __str__(self):
		return self.teamone + " v " + self.teamtwo + " - " + self.gamedate.strftime("%m/%d/%Y")


class Player(models.Model):
	club = models.ForeignKey(Club,null=True, on_delete = models.SET_NULL)
	name =  models.CharField(max_length = 30, null = True)
	number = models.IntegerField(null = True)
	position = 	models.CharField(max_length = 10, null = True)
	nation = models.CharField(max_length = 30, null = True)
	picture = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name
