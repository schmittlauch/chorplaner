# -*- coding: latin-1 -*-
from poll.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):# Choice auf der Poll-Bearbeitungsseite
    model = Choice
    extra = 3                           #es werden 3 leere Felder bereitgestellt

class PollAdmin(admin.ModelAdmin):      #definiert Aussehen der Poll-Bearbeitungsseite
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        #collapse bedeutet: standardmaessig ausgeblendet
    ]
    inlines = [ChoiceInline]            #einbinden des inlines
    list_display = ('question', 'pub_date',"was_published_today")#was wird auf der auswahlseite angezeigt?
    list_filter = ['pub_date']          #Filterleiste am Rand
    search_fields = ['question']
    date_hierarchy = 'pub_date'         #Datumsnavigationsbaum

admin.site.register(Poll, PollAdmin)