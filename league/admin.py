from django.contrib import admin

from .models import User, Player, PlayerSelection, PlayerStats, Team, Matchup, Bracket

# Register your models here.
admin.site.register(User)
admin.site.register(Player)
admin.site.register(PlayerSelection)
admin.site.register(PlayerStats)
admin.site.register(Team)
admin.site.register(Matchup)
admin.site.register(Bracket)
