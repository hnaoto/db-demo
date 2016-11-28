from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from .models import Defense
from .models import Team
from .models import Players
from .models import PlayerRank
from .models import Kicker
from .models import Consistency
from .models import Injury
from .models import Suspended
from .models import CareerStats
from .models import SeasonOffensiveStats
from django.db import connection,transaction

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]

def index(request):
    name = request.GET.get("n")
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM dbdemo_Players WHERE name =%s''',[name])

    playerSet  = dictfetchall(cursor)

    cursor.execute('''SELECT * FROM dbdemo_Team WHERE name =%s''',[name])
    teamSet = dictfetchall(cursor)

    cursor.close()
    context ={
        "player_list": playerSet,
        "team_list": teamSet,

    }
    return render(request,'index.html', context)