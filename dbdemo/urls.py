from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^advanceSearch/$',views.advanceSearch,name='advanceSearch'),
    url(r'^advanceSearch/changeCriteria/',views.changeTable,name='changeTable'),
    url(r'^advanceSearch/search/$',views.advanceSearchAction,name='advanceSearchAction'),
    url(r'^Injury/Detail/(?P<person_id>.*)/$', views.injuryDetail, name='injuryDetail'),
    url(r'^Suspended/Detail/(?P<person_id>.*)/$', views.suspendedDetail, name='suspendedDetail'),
    url(r'^Kicker/Detail/(?P<person_id>.*)/$', views.kickerDetail, name='kickerDetail')


]