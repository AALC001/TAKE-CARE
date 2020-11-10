from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Agent, AgentCategory


class AgentAdmin(VersionAdmin,admin.ModelAdmin):
    def compte_dossiers_out(self):
        return len(self.mouvements.filter(dossier__state__description='out'))
    compte_dossiers_out.short_description ="Dossiers empruntés"
    
    list_display = ['categorie_agent','code',
                        'nom' ,'prenoms',compte_dossiers_out]


class AgentInline(admin.TabularInline):
    model = Agent
    readonly_fields = ['code', 
            'nom','prenoms']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class AgentCategoryAdmin(VersionAdmin, admin.ModelAdmin):
    inlines = [AgentInline,]

admin.site.register(Agent, AgentAdmin)
admin.site.register(AgentCategory, AgentCategoryAdmin)