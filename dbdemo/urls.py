from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^advanceSearch/$',views.advanceSearch,name='advanceSearch'),
    url(r'^compareList/$',views.compareList,name='compareList'),
    url(r'^Injury/Detail/(?P<person_id>.*)/$', views.injuryDetail, name='injuryDetail'),
    url(r'^Suspended/Detail/(?P<person_id>.*)/$', views.suspendedDetail, name='suspendedDetail'),
    url(r'^Kicker/Detail/(?P<person_id>.*)/$', views.kickerDetail, name='kickerDetail'),

    url(r'^advanceSearch/Player/$',views.Player,name='Player'),
    url(r'^advanceSearch/PlayerRank/$',views.PlayerRank,name='PlayerRank'),
    url(r'^advanceSearch/Consistency/$',views.Consistency,name='Consistency'),
    url(r'^advanceSearch/Kicker/$',views.Kicker,name='Kicker'),
    url(r'^advanceSearch/CareerStats/$',views.CareerStats,name='CareerStats'),
    url(r'^advanceSearch/SeasonOffensiveStats/$',views.SeasonOffensiveStats,name='SeasonOffensiveStats'),
    
    url(r'^players/$',views.players_show),
]

