from django.db import models

# Create your models here.



class Player(models.Model):
	player_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	position = models.CharField(max_length=50)
	def __unicode__(self):
		return self.first_name+" "+self.last_name 

class PlayerGeneral(models.Model):
	player = models.ForeignKey(Player, related_name='playergen')
	league_average = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
		return self.player.first_name+" "+self.player.last_name 

class PlayerStaticsGame(models.Model):
	player = models.ForeignKey(Player, related_name='playergame')
	valoration = models.IntegerField()
	points = models.IntegerField()
	rebounds = models.IntegerField()
	assists = models.IntegerField()
	def __unicode__(self):
		return self.player.first_name+" "+self.player.last_name 
	

class Team(models.Model):
	team_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	division = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	league_position = models.IntegerField()
	def __unicode__(self):
		return self.name+", "+self.city+", "+self.division+", "+str(self.league_position)

class TeamGeneral(models.Model):
	team = models.ForeignKey(Team, related_name='teamgen')
	players = models.ManyToManyField(PlayerGeneral)
	def __unicode__(self):
		return self.team.name+", "+self.team.city+", "+self.team.division+", "+str(self.team.league_position)	

class TeamStaticsGame(models.Model):
	team = models.ForeignKey(Team, related_name='teamgame')
	players = models.ManyToManyField(PlayerStaticsGame)
	def __unicode__(self):
		return self.team.name+", "+self.team.city+", "+self.team.division+", "+str(self.team.league_position)	



class Game(models.Model):
	game_id = models.IntegerField(primary_key=True, unique=True)
	local = models.ForeignKey(TeamStaticsGame, related_name='local')
	visitor = models.ForeignKey(TeamStaticsGame, related_name='visitor')
	date = models.DateField()
	result = models.CharField(max_length=50)
	def __unicode__(self):
		return self.local.team.name+" vs "+self.visitor.team.name+": "+str(self.date)

class League(models.Model):
	league_id = models.AutoField(primary_key=True)
	league_name = models.CharField(max_length=3)
	country = models.CharField(max_length=50)
	league_players = models.ManyToManyField(PlayerGeneral)
	league_teams = models.ManyToManyField(TeamGeneral)
	league_games = models.ManyToManyField(Game)
	def __unicode__(self):
		return self.league_name
	

	
