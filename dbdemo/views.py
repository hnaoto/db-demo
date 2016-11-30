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
from django.template import RequestContext
from .forms import PlayerForm, ConsistencyForm,PlayerRankForm,KickerForm,CareerStatsForm,SeasonOffensiveStatsForm
import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection,transaction

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]

def index(request):
    print('submited')
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


def compareList(request):
    print('submited')
    name = request.COOKIES.get('pOne')
    InjurySet1={}
    SuspendedSet1 = {}
    RankSet1 = {}
    ConsistencySet1 = {}
    SeasonSet1 = {}
    CareerSet1 = {}
    Kicker1 = {}
    teamBelong1 = {}

    InjurySet2={}
    SuspendedSet2 = {}
    RankSet2 = {}
    ConsistencySet2 = {}
    SeasonSet2 = {}
    CareerSet2 = {}
    Kicker2 = {}
    teamBelong2 = {}

    if name:
        cursor = connection.cursor()

        cursor.execute('''SELECT * FROM dbdemo_Players WHERE name =%s''',[name])

        playerSet1  = dictfetchall(cursor)


        if playerSet1:
            playerID = playerSet1[0]['id']

            cursor.execute('''SELECT t.name AS name
                              FROM dbdemo_Team AS t,dbdemo_Players AS p,dbdemo_TeamPlayerRelation AS c
                              WHERE t.id = c.teamID_id AND p.id = c.pid_id AND p.id = %s''',[playerID])

            teamBelong1 = dictfetchall(cursor)


            cursor.execute('''SELECT *
                      FROM dbdemo_Injury AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])
            InjurySet1 = dictfetchall(cursor)

            cursor.execute('''SELECT *
                      FROM dbdemo_Suspended AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])
            SuspendedSet1 = dictfetchall(cursor)

            cursor.execute('''SELECT *
                              FROM dbdemo_PlayerRank AS r
                              Where EXISTS
                                (SELECT *
                                FROM dbdemo_Players as p
                                WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            RankSet1 = dictfetchall(cursor)


            cursor.execute('''SELECT *
                      FROM dbdemo_Consistency AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            ConsistencySet1 = dictfetchall(cursor)


            cursor.execute('''SELECT *
              FROM dbdemo_SeasonOffensiveStats AS r
              Where EXISTS
                (SELECT *
                FROM dbdemo_Players as p
                WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            SeasonSet1 = dictfetchall(cursor)


            cursor.execute('''SELECT *
                      FROM dbdemo_CareerStats AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            CareerSet1 = dictfetchall(cursor)


            cursor.execute('''SELECT *
              FROM dbdemo_Kicker AS r
              Where EXISTS
                (SELECT *
                FROM dbdemo_Players as p
                WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            Kicker1 = dictfetchall(cursor)


        name = request.COOKIES.get('pTwo')
        if name:
                    cursor.execute('''SELECT * FROM dbdemo_Players WHERE name =%s''',[name])

        playerSet2  = dictfetchall(cursor)


        if playerSet2:
            playerID = playerSet2[0]['id']

            cursor.execute('''SELECT t.name AS name
                              FROM dbdemo_Team AS t,dbdemo_Players AS p,dbdemo_TeamPlayerRelation AS c
                              WHERE t.id = c.teamID_id AND p.id = c.pid_id AND p.id = %s''',[playerID])

            teamBelong2 = dictfetchall(cursor)


            cursor.execute('''SELECT *
                      FROM dbdemo_Injury AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])
            InjurySet2 = dictfetchall(cursor)

            cursor.execute('''SELECT *
                      FROM dbdemo_Suspended AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])
            SuspendedSet2 = dictfetchall(cursor)

            cursor.execute('''SELECT *
                              FROM dbdemo_PlayerRank AS r
                              Where EXISTS
                                (SELECT *
                                FROM dbdemo_Players as p
                                WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            RankSet2 = dictfetchall(cursor)


            cursor.execute('''SELECT *
                      FROM dbdemo_Consistency AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            ConsistencySet2 = dictfetchall(cursor)


            cursor.execute('''SELECT *
              FROM dbdemo_SeasonOffensiveStats AS r
              Where EXISTS
                (SELECT *
                FROM dbdemo_Players as p
                WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            SeasonSet2 = dictfetchall(cursor)


            cursor.execute('''SELECT *
                      FROM dbdemo_CareerStats AS r
                      Where EXISTS
                        (SELECT *
                        FROM dbdemo_Players as p
                        WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            CareerSet2 = dictfetchall(cursor)


            cursor.execute('''SELECT *
              FROM dbdemo_Kicker AS r
              Where EXISTS
                (SELECT *
                FROM dbdemo_Players as p
                WHERE r.pid_id = p.id AND p.id = %s)''',[playerID])

            Kicker2 = dictfetchall(cursor)







    cursor.close()
    context ={
        "player_list1": playerSet1,
        "TeamBelong_list1":teamBelong1,
        "Injury_list1": InjurySet1,
        "Suspended_list1": SuspendedSet1,
        "Consistency_list1": ConsistencySet1,
        "Season_list1": SeasonSet1,
        "Career_list1": CareerSet1,
        "Kicker_list1": Kicker1,
        "Rank_list1":RankSet1,
        "player_list2": playerSet2,
        "TeamBelong_list2":teamBelong2,
        "Injury_list2": InjurySet2,
        "Suspended_list2": SuspendedSet2,
        "Consistency_list2": ConsistencySet2,
        "Season_list2": SeasonSet2,
        "Career_list2": CareerSet2,
        "Kicker_list2": Kicker2,
        "Rank_list2":RankSet2,

    }
    return render(request,'compare.html', context)


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



def advanceSearch(request):

    playerRankForm = PlayerRankForm(request.POST or None)
    playerForm = PlayerForm(request.POST or None)
    consistencyForm = ConsistencyForm(request.POST or None)
    kickerForm = KickerForm(request.POST or None)
    careerStatsForm = CareerStatsForm(request.POST or None)
    seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




    context={
        "PlayerRankForm":playerRankForm,
        "PlayerForm":playerForm,
        "ConsistencyForm":consistencyForm,
        "KickerForm":kickerForm,
        "CareerStatsForm":careerStatsForm,
        "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
        "existence":True,
    }
    return render(request,'advanceSearch.html',context)
    # context = {
    #     "existence":False,
    # }
    # return render( request,'advanceSearch.html',context)



#
# context={
#         "PlayerRankForm":playerRankForm,
#         "PlayerForm":playerForm,
#         "ConsistencyForm":consistencyForm,
#         "KickerForm":kickerForm,
#         "CareerStatsForm":careerStatsForm,
#         "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
#         "existence":True,
#     }


def Player(request):
    form = PlayerForm(request.POST or None)

    if form.is_valid():
        exp = form.cleaned_data.get('experience')
        position = form.cleaned_data.get('position')
    exp = int(exp)
    cursor = connection.cursor()
    sql = '''SELECT name
          FROM dbdemo_Players AS p
          Where p.experience > %d
          AND p.position = "%s"'''% (int(exp),position)
    cursor.execute(sql)
    result = dictfetchall(cursor)
    if result:
        # print(result[0].get('name'))
        # url = '/?n=%s'% result[0].get('name')
        context={
            "player_list":result,
        }

        return render(request,'playerMatchingCriteria.html',context)

    else:

        playerRankForm = PlayerRankForm(request.POST or None)
        playerForm = PlayerForm(request.POST or None)
        consistencyForm = ConsistencyForm(request.POST or None)
        kickerForm = KickerForm(request.POST or None)
        careerStatsForm = CareerStatsForm(request.POST or None)
        seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




        context={
            "PlayerRankForm":playerRankForm,
            "PlayerForm":playerForm,
            "ConsistencyForm":consistencyForm,
            "KickerForm":kickerForm,
            "CareerStatsForm":careerStatsForm,
            "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
            "existence":False,
        }
        return render(request,'advanceSearch.html',context)

def PlayerRank(request):
    form = PlayerRankForm(request.POST or None)

    if form.is_valid():
        espn = form.cleaned_data.get('espnRank')
        nfl = form.cleaned_data.get('nflRank')
        pos = form.cleaned_data.get('sugPos')


    cursor = connection.cursor()
    sql = '''SELECT name
          FROM dbdemo_Players AS p
          Where EXISTS (
          SELECT *
          FROM dbdemo_PlayerRank as r
          WHERE r.sugPos = "%s"
          AND r.espnRank < %d
          AND r.nflRank < %d
          AND p.id = r.pid_id)'''% (pos,espn,nfl)
    print(sql)
    cursor.execute(sql)
    result = dictfetchall(cursor)
    if result:
        # print(result[0].get('name'))
        # url = '/?n=%s'% result[0].get('name')
        context={
            "player_list":result,
        }

        return render(request,'playerMatchingCriteria.html',context)


    else:

        playerRankForm = PlayerRankForm(request.POST or None)
        playerForm = PlayerForm(request.POST or None)
        consistencyForm = ConsistencyForm(request.POST or None)
        kickerForm = KickerForm(request.POST or None)
        careerStatsForm = CareerStatsForm(request.POST or None)
        seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




        context={
            "PlayerRankForm":playerRankForm,
            "PlayerForm":playerForm,
            "ConsistencyForm":consistencyForm,
            "KickerForm":kickerForm,
            "CareerStatsForm":careerStatsForm,
            "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
            "existence":False,
        }
        return render(request,'advanceSearch.html',context)


def Consistency(request):
    form = ConsistencyForm(request.POST or None)

    if form.is_valid():
        score = form.cleaned_data.get('score')
        elite = form.cleaned_data.get('eliteScore')
        top = form.cleaned_data.get('topScore')
        subpar = form.cleaned_data.get('subparScore')


    cursor = connection.cursor()
    sql = '''SELECT name
          FROM dbdemo_Players AS p
          Where EXISTS (
          SELECT *
          FROM dbdemo_Consistency as r
          WHERE r.score > %d
          AND r.eliteScore > %d
          AND r.topScore > %d
          AND r.subparScore > %d
          AND p.id = r.pid_id)'''% (score,elite,top,subpar)
    print(sql)
    cursor.execute(sql)
    result = dictfetchall(cursor)
    if result:
        # print(result[0].get('name'))
        # url = '/?n=%s'% result[0].get('name')
        context={
            "player_list":result,
        }

        return render(request,'playerMatchingCriteria.html',context)

    else:

        playerRankForm = PlayerRankForm(request.POST or None)
        playerForm = PlayerForm(request.POST or None)
        consistencyForm = ConsistencyForm(request.POST or None)
        kickerForm = KickerForm(request.POST or None)
        careerStatsForm = CareerStatsForm(request.POST or None)
        seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




        context={
            "PlayerRankForm":playerRankForm,
            "PlayerForm":playerForm,
            "ConsistencyForm":consistencyForm,
            "KickerForm":kickerForm,
            "CareerStatsForm":careerStatsForm,
            "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
            "existence":False,
        }
        return render(request,'advanceSearch.html',context)


def Kicker(request):
    form = KickerForm(request.POST or None)

    if form.is_valid():
        fd = form.cleaned_data.get('fg')
        fga = form.cleaned_data.get('fga')
        xpa = form.cleaned_data.get('xpa')
        xp = form.cleaned_data.get('xp')


    cursor = connection.cursor()
    sql = '''SELECT name
          FROM dbdemo_Players AS p
          Where EXISTS (
          SELECT *
          FROM dbdemo_Kicker as r
          WHERE r.fg > %d
          AND r.fga > %d
          AND r.xpa > %d
          AND r.xp > %d
          AND p.id = r.pid_id)'''% (fd,fga,xpa,xp)
    print(sql)
    cursor.execute(sql)
    result = dictfetchall(cursor)
    if result:
        # print(result[0].get('name'))
        # url = '/?n=%s'% result[0].get('name')
        context={
            "player_list":result,
        }

        return render(request,'playerMatchingCriteria.html',context)

    else:

        playerRankForm = PlayerRankForm(request.POST or None)
        playerForm = PlayerForm(request.POST or None)
        consistencyForm = ConsistencyForm(request.POST or None)
        kickerForm = KickerForm(request.POST or None)
        careerStatsForm = CareerStatsForm(request.POST or None)
        seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




        context={
            "PlayerRankForm":playerRankForm,
            "PlayerForm":playerForm,
            "ConsistencyForm":consistencyForm,
            "KickerForm":kickerForm,
            "CareerStatsForm":careerStatsForm,
            "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
            "existence":False,
        }
        return render(request,'advanceSearch.html',context)


def CareerStats(request):
    form = CareerStatsForm(request.POST or None)

    if form.is_valid():
        ps = form.cleaned_data.get('pointScored')
        py = form.cleaned_data.get('passYards')
        ry = form.cleaned_data.get('rushYards')
        recYards = form.cleaned_data.get('recYards')
        rTD = form.cleaned_data.get('rushTDs')
        recTDs = form.cleaned_data.get('recTDs')
        inter = form.cleaned_data.get('interceptions')
        f = form.cleaned_data.get('fumblesLost')
        tp = form.cleaned_data.get('twoPtConversion')
        passTDs = form.cleaned_data.get('passTDs')


    cursor = connection.cursor()
    sql = '''SELECT name
          FROM dbdemo_Players AS p
          Where EXISTS (
          SELECT *
          FROM dbdemo_CareerStats as r
          WHERE r.pointScored > %d
          AND r.passYards > %d
          AND r.rushYards > %d
          AND r.recYards > %d
          AND r.rushTDs > %d
          AND r.recTDs > %d
          AND r.interceptions < %d
          AND r.fumblesLost < %d
          AND r.twoPtConversion > %d
          AND r.passTDs > %d
          AND p.id = r.pid_id)'''% (ps,py,ry,recYards,rTD,recTDs,inter,f,tp,passTDs)
    print(sql)
    cursor.execute(sql)
    result = dictfetchall(cursor)
    if result:
        # print(result[0].get('name'))
        # url = '/?n=%s'% result[0].get('name')
        context={
            "player_list":result,
        }

        return render(request,'playerMatchingCriteria.html',context)

    else:

        playerRankForm = PlayerRankForm(request.POST or None)
        playerForm = PlayerForm(request.POST or None)
        consistencyForm = ConsistencyForm(request.POST or None)
        kickerForm = KickerForm(request.POST or None)
        careerStatsForm = CareerStatsForm(request.POST or None)
        seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




        context={
            "PlayerRankForm":playerRankForm,
            "PlayerForm":playerForm,
            "ConsistencyForm":consistencyForm,
            "KickerForm":kickerForm,
            "CareerStatsForm":careerStatsForm,
            "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
            "existence":False,
        }
        return render(request,'advanceSearch.html',context)


def SeasonOffensiveStats(request):
    form = CareerStatsForm(request.POST or None)

    if form.is_valid():
        ps = form.cleaned_data.get('pointScored')
        py = form.cleaned_data.get('passYards')
        ry = form.cleaned_data.get('rushYards')
        recYards = form.cleaned_data.get('recYards')
        rTD = form.cleaned_data.get('rushTDs')
        recTDs = form.cleaned_data.get('recTDs')
        inter = form.cleaned_data.get('interceptions')
        f = form.cleaned_data.get('fumblesLost')
        tp = form.cleaned_data.get('twoPtConversion')
        passTDs = form.cleaned_data.get('passTDs')


    cursor = connection.cursor()
    sql = '''SELECT name
          FROM dbdemo_Players AS p
          Where EXISTS (
          SELECT *
          FROM dbdemo_SeasonOffensiveStats as r
          WHERE r.pointScored > %d
          AND r.passYards > %d
          AND r.rushYards > %d
          AND r.recYards > %d
          AND r.rushTDs > %d
          AND r.recTDs > %d
          AND r.interceptions < %d
          AND r.fumblesLost < %d
          AND r.twoPtConversion > %d
          AND r.passTDs > %d
          AND p.id = r.pid_id)'''% (ps,py,ry,recYards,rTD,recTDs,inter,f,tp,passTDs)
    print(sql)
    cursor.execute(sql)
    result = dictfetchall(cursor)
    if result:
        # print(result[0].get('name'))
        # url = '/?n=%s'% result[0].get('name')
        context={
            "player_list":result,
        }

        return render(request,'playerMatchingCriteria.html',context)

    else:

        playerRankForm = PlayerRankForm(request.POST or None)
        playerForm = PlayerForm(request.POST or None)
        consistencyForm = ConsistencyForm(request.POST or None)
        kickerForm = KickerForm(request.POST or None)
        careerStatsForm = CareerStatsForm(request.POST or None)
        seasonOffensiveStatsForm = SeasonOffensiveStatsForm(request.POST or None)




        context={
            "PlayerRankForm":playerRankForm,
            "PlayerForm":playerForm,
            "ConsistencyForm":consistencyForm,
            "KickerForm":kickerForm,
            "CareerStatsForm":careerStatsForm,
            "SeasonOffensiveStatsForm":seasonOffensiveStatsForm,
            "existence":False,
        }
        return render(request,'advanceSearch.html',context)