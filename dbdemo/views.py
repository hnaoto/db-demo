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
from .models import TeamPlayerRelation
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

    InjurySet={}
    SuspendedSet = {}
    RankSet = {}
    ConsistencySet = {}
    SeasonSet = {}
    CareerSet = {}
    Kicker = {}
    teamBelong = {}
    if playerSet:
        playerID = playerSet[0]['id']

        cursor.execute('''SELECT t.name AS name
                          FROM dbdemo_Team AS t,dbdemo_Players AS p,dbdemo_TeamPlayerRelation AS c
                          WHERE t.id = c.teamID_id AND p.id = c.pid_id AND p.id = %s''',[playerID])

        teamBelong = dictfetchall(cursor)


        cursor.execute('''SELECT *
                  FROM dbdemo_Injury AS r
                  Where EXISTS
                    (SELECT *
                    FROM dbdemo_Players as p
                    WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])
        InjurySet = dictfetchall(cursor)

        cursor.execute('''SELECT *
                  FROM dbdemo_Suspended AS r
                  Where EXISTS
                    (SELECT *
                    FROM dbdemo_Players as p
                    WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])
        SuspendedSet = dictfetchall(cursor)

        cursor.execute('''SELECT *
                          FROM dbdemo_PlayerRank AS r
                          Where EXISTS
                            (SELECT *
                            FROM dbdemo_Players as p
                            WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

        RankSet = dictfetchall(cursor)


        cursor.execute('''SELECT *
                  FROM dbdemo_Consistency AS r
                  Where EXISTS
                    (SELECT *
                    FROM dbdemo_Players as p
                    WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

        ConsistencySet = dictfetchall(cursor)


        cursor.execute('''SELECT *
          FROM dbdemo_SeasonOffensiveStats AS r
          Where EXISTS
            (SELECT *
            FROM dbdemo_Players as p
            WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

        SeasonSet = dictfetchall(cursor)


        cursor.execute('''SELECT *
                  FROM dbdemo_CareerStats AS r
                  Where EXISTS
                    (SELECT *
                    FROM dbdemo_Players as p
                    WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

        CareerSet = dictfetchall(cursor)


        cursor.execute('''SELECT *
          FROM dbdemo_Kicker AS r
          Where EXISTS
            (SELECT *
            FROM dbdemo_Players as p
            WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

        Kicker = dictfetchall(cursor)

        print(RankSet)





    cursor.execute('''SELECT * FROM dbdemo_Team WHERE name =%s''',[name])
    teamSet = dictfetchall(cursor)

    print(teamSet)
    contractSet = {}
    defenseSet = {}


    if teamSet:
        teamID = teamSet[0]['id']
        print(teamID)
        cursor.execute('''SELECT p.id AS playerID,p.name AS playerName
                          FROM dbdemo_Team AS t,dbdemo_Players AS p,dbdemo_TeamPlayerRelation AS c
                          WHERE t.id = c.teamID_id AND p.id = c.pid_id AND t.id = %s''',[teamID])

    # cursor.execute('''SELECT * FROM dbdemo_TeamPlayerRelation''')

        contractSet = dictfetchall(cursor)

        cursor.execute('''SELECT *
                          FROM dbdemo_Defense AS i,dbdemo_Team AS p
                          WHERE p.id = i.teamID_id AND p.id = %s''',[teamID])

        defenseSet = dictfetchall(cursor)

    print(contractSet)
    cursor.close()
    context ={
        "player_list": playerSet,
        "TeamBelong_list":teamBelong,
        "Injury_list": InjurySet,
        "Suspended_list": SuspendedSet,
        "Consistency_list": ConsistencySet,
        "Season_list": SeasonSet,
        "Career_list": CareerSet,
        "Kicker_list": Kicker,
        "Rank_list":RankSet,
        "team_list": teamSet,
        "contract_list": contractSet,
        "defense_list":defenseSet,

    }
    return render(request,'index.html', context)

def injuryDetail(request,person_id):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
          FROM dbdemo_Injury AS r
          Where EXISTS
            (SELECT *
            FROM dbdemo_Players as p
            WHERE r.pid_id = p.id AND p.id = %s)''',[person_id])
    InjurySet = dictfetchall(cursor)
    cursor.execute('''SELECT name
                      FROM dbdemo_Players AS p
                      WHERE p.id=%s''',[person_id])
    pName = dictfetchall(cursor)
    context = {
        "Injury_list":InjurySet,
        "name_list":pName,
    }

    cursor.close()
    return render(request,'injuryDetail.html', context)


def suspendedDetail(request,person_id):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
          FROM dbdemo_Suspended AS r
          Where EXISTS
            (SELECT *
            FROM dbdemo_Players as p
            WHERE r.pid_id = p.id AND p.id = %s)''',[person_id])
    SuspendSet = dictfetchall(cursor)
    cursor.execute('''SELECT name
                      FROM dbdemo_Players AS p
                      WHERE p.id=%s''',[person_id])
    pName = dictfetchall(cursor)
    context = {
        "Suspend_list":SuspendSet,
        "name_list":pName,
    }

    cursor.close()
    return render(request,'suspendedDetail.html', context)


def kickerDetail(request,person_id):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
          FROM dbdemo_Kicker AS r
          Where EXISTS
            (SELECT *
            FROM dbdemo_Players as p
            WHERE r.pid_id = p.id AND p.id = %s)''',[person_id])
    KickerSet = dictfetchall(cursor)
    cursor.execute('''SELECT name
                      FROM dbdemo_Players AS p
                      WHERE p.id=%s''',[person_id])
    pName = dictfetchall(cursor)
    context = {
        "Kicker_list":KickerSet,
        "name_list":pName,
    }

    cursor.close()
    return render(request,'kickerDetail.html', context)










