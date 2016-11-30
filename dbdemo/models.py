from django.db import models

# Create your models here.





class Team(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    def __str__(self):
        return "%s at %s" % (self.name,self.city)

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
    teamID = models.ForeignKey(Team,null=True)
    def __str__(self):
        return "%s" % (self.teamID.name)



class Players(models.Model):
    POSITION_CHOICE=(
        ('QB','Quater Back'),
        ('RB','Running Back'),
        ('WR','Wide Receiver'),
        ('TE','Tight End'),
    )
    name = models.CharField(max_length=20)
    experience = models.IntegerField(default=0)
    position = models.CharField(max_length=2,choices=POSITION_CHOICE)
    def __str__(self):
        return "%s" % (self.name)


class TeamPlayerRelation(models.Model):
    teamId = models.ForeignKey(Team)
    pid = models.ForeignKey(Players)
    def __str__(self):
        return "%s contract with player: %s" % (self.teamId.name,self.pid.name)

class PlayerRank(models.Model):
    POSITION_CHOICE=(
        ('QB','Quater Back'),
        ('RB','Running Back'),
        ('WR','Wide Receiver'),
        ('TE','Tight End'),
    )
    pid = models.ForeignKey(Players)
    espnRank = models.IntegerField(default=-1)
    nflRank = models.IntegerField(default=-1)
    sugPos = models.CharField(max_length=3,choices=POSITION_CHOICE)
    def __str__(self):
        return "%s" % (self.pid.name)



class Kicker(models.Model):

    fg = models.IntegerField(default=0)
    fga = models.IntegerField(default=0)
    xpa = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    pid = models.ForeignKey(Players)
    def __str__(self):
        return "%s" % (self.pid.name)


class Consistency(models.Model):
    pid = models.ForeignKey(Players,null=True)
    score = models.FloatField(default=0)
    eliteScore = models.FloatField(default=0)
    topScore = models.FloatField(default=0)
    subparScore = models.FloatField(default=0)
    def __str__(self):
        return "%s" % (self.pid.name)


class Injury(models.Model):

    ir = models.BooleanField(default=False)
    status = models.CharField(max_length=5)
    dfy = models.BooleanField(default=False)
    injuryName = models.CharField(max_length=20)
    pid = models.ForeignKey(Players)
    def __str__(self):
        return "%s" % (self.pid.name)

class Suspended(models.Model):
    pid = models.ForeignKey(Players)
    reasons = models.CharField(max_length=50)
    status = models.CharField(max_length=5)
    susLength = models.IntegerField(default=0)
    dfy = models.BooleanField(default=False)
    def __str__(self):
        return "%s" % (self.pid.name)


class SeasonOffensiveStats(models.Model):
    pid = models.ForeignKey(Players)
    pointScored = models.IntegerField(default=0)
    passYards  = models.IntegerField(default=0)
    rushYards = models.IntegerField(default=0)
    recYards = models.IntegerField(default=0)
    rushTDs = models.IntegerField(default=0)
    recTDs = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    fumblesLost = models.IntegerField(default=0)
    twoPtConversion = models.IntegerField(default=0)
    passTDs = models.IntegerField(default=0)
    def __str__(self):
        return "%s" % (self.pid.name)

class CareerStats(models.Model):
    pid = models.ForeignKey(Players)
    pointScored = models.IntegerField(default=0)
    passYards  = models.IntegerField(default=0)
    rushYards = models.IntegerField(default=0)
    recYards = models.IntegerField(default=0)
    rushTDs = models.IntegerField(default=0)
    recTDs = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    fumblesLost = models.IntegerField(default=0)
    twoPtConversion = models.IntegerField(default=0)
    passTDs = models.IntegerField(default=0)
    def __str__(self):
        return "%s" % (self.pid.name)


