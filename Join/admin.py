from django.contrib import admin
from .models import Join

class JoinAdmin(admin.ModelAdmin):
    list_display = ['__str__','varEmail', 'varTimestamp', 'varUpdated']
    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)