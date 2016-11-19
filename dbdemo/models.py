from django.db import models

# Create your models here.



class Defense(models.Model):
    pointsAllowed = models.IntegerField(default=0)
    sacks = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    fumbleRecoveries = models.IntegerField(default=0)
    defTD = models.IntegerField(default=0)
    passRank = models.IntegerField(default=0)
    rushRank = models.IntegerField(default=0)
    puntRetRank = models.IntegerField(default=0)
    kickRetRank = models.IntegerField(default=0)

class Team(models.Model):
    name = models.CharField(max_length=30)
    # city = models.CharField(max_length=30)
    defenseID = models.ForeignKey(Defense, default=-1)