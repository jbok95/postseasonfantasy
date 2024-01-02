from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return self.username

class PlayerStats(models.Model):
    week = models.IntegerField()
    
    passing_yards = models.IntegerField(default=0)
    passing_touchdowns = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)

    rushing_yards = models.IntegerField(default=0)
    rushing_touchdowns = models.IntegerField(default=0)
    rushing_fumbles = models.IntegerField(default=0)

    receiving_yards = models.IntegerField(default=0)
    receiving_touchdowns = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)

    two_point_conversions = models.IntegerField(default=0)
    other_touchdowns = models.IntegerField(default=0)

    def calculate_total_points(self):
        passing_points = self.passing_yards / 25 + self.passing_touchdowns * 4 - self.interceptions * 2
        rushing_points = self.rushing_yards / 10 + self.rushing_touchdowns * 6 - self.rushing_fumbles * 2
        receiving_points = self.receiving_yards / 10 + self.receiving_touchdowns * 6 + self.receptions / 2
        other_points = self.two_point_conversions * 2 + self.other_touchdowns * 6

        total_points = passing_points + rushing_points + receiving_points + other_points
        return total_points

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    stats = models.OneToOneField(PlayerStats, related_name="player_stats", on_delete=models.CASCADE, null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=100, default="")
    owner = models.ForeignKey(User, related_name="team_owner", on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name="team_roster", through='PlayerSelection')

class PlayerSelection(models.Model):
    team = models.ForeignKey(Team, related_name="player_team", on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="player", on_delete=models.CASCADE)
    week = models.IntegerField()

class Matchup(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    week = models.IntegerField()
    result = models.CharField(max_length=10)

class Bracket(models.Model):
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
