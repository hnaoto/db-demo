from django import forms
from django.db import models
from .models import Players
from .models import PlayerRank
from .models import Kicker
from .models import Consistency
from .models import CareerStats
from .models import SeasonOffensiveStats


class PlayerForm(forms.ModelForm):



    class Meta:
        model = Players
        fields = ['experience','position']
        # widgets={
        #     'position':forms.RadioSelect
        # }

class PlayerRankForm(forms.ModelForm):

    class Meta:
        model = PlayerRank
        fields = ['espnRank','nflRank','sugPos']
        # widgets={
        #     'position':forms.RadioSelect
        # }

class KickerForm(forms.ModelForm):
    class Meta:
        model = Kicker
        exclude=['id','pid_id','pid']

class ConsistencyForm(forms.ModelForm):
    class Meta:
        model = Consistency
        exclude = ['id','pid_id','pid']

class CareerStatsForm(forms.ModelForm):
    class Meta:
        model = CareerStats
        exclude = ['id','pid_id','pid']

class SeasonOffensiveStatsForm(forms.ModelForm):
    class Meta:
        model = SeasonOffensiveStats
        exclude = ['id','pid_id','pid']