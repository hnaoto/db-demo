from django.contrib import admin

# Register your models here.

from django.contrib import admin
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

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','position')

admin.site.register(Defense)
admin.site.register(Team)
admin.site.register(Players,PlayerAdmin)
admin.site.register(PlayerRank)
admin.site.register(Kicker)
admin.site.register(Consistency)
admin.site.register(Injury)
admin.site.register(Suspended)
admin.site.register(CareerStats)
admin.site.register(SeasonOffensiveStats)
admin.site.register(TeamPlayerRelation)