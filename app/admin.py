from django.contrib import admin
from .models import SeriesName, CharacterInfo, UserSeries, UserCharacter



class CharacterId(admin.ModelAdmin):
    readonly_fields = ('id', )

class CharacterId2(admin.ModelAdmin):
    readonly_fields = ('id', )


admin.site.register(SeriesName, CharacterId2)
admin.site.register(CharacterInfo, CharacterId)
admin.site.register(UserSeries, CharacterId2)
admin.site.register(UserCharacter, CharacterId)
