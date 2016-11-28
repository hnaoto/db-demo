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



def index(request):
 querySet  = Defense.objects.all()
 context ={
   "object_list": querySet

 }
 return render(request,'index.html', context)