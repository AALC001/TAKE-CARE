from django.contrib import admin
from .models import Patient
from relance.models import *
#from reversion.admin import VersionAdmin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export import resources,fields,widgets
# Register your models here.


class RendezVousInline(admin.TabularInline):
	model = RendezVous

class SuiviRdvARVInline(admin.TabularInline):
	model = SuiviRdvARV

class ContactSujetIndexInline(admin.TabularInline):
	model = ContactSujetIndex


class PatientResource(resources.ModelResource):
	age = fields.Field(attribute='age')
	class Meta:
		model = Patient
		import_id_fields = ('code_patient',)
		#exclude = ('id', 'creation_time', 'update_time', )
		fields=('code_patient', 'presence_soins','nom_prenoms', 'sexe', 'date_naissance', 'age','statut_ARV','date_dernier_RDV_CV',
		'nb_jour_CV','resultat_derniere_CV','date_dernier_RDV_ARV','nb_jour_ARV','date_dernier_RDV_ETP','nb_jour_ETP','nom_conseiller',)
		
		export_order=('code_patient', 'presence_soins','nom_prenoms', 'sexe', 'date_naissance', 'age','statut_ARV','date_dernier_RDV_CV',
		'nb_jour_CV','resultat_derniere_CV','date_dernier_RDV_ARV','nb_jour_ARV','date_dernier_RDV_ETP','nb_jour_ETP','nom_conseiller',)


class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = PatientResource
	list_display = ('code_patient', 'presence_soins','nom_prenoms', 'sexe', 'date_naissance', 'age', 'statut_ARV','date_dernier_RDV_CV',
		'nb_jour_CV','resultat_derniere_CV','date_dernier_RDV_ARV','nb_jour_ARV','date_dernier_RDV_ETP','nb_jour_ETP','nom_conseiller',)
	search_fields=['code_patient',  'nom_prenoms']

	inlines = [
		RendezVousInline,
		ContactSujetIndexInline,
	]

admin.site.register(Patient, PatientAdmin,)