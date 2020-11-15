from django.contrib import admin
from .models import Patient
from relance.models import *
#from reversion.admin import VersionAdmin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export import resources,fields,widgets
# Register your models here.


class ChargeViraleInline(admin.TabularInline):
	model = ChargeVirale

class ContactSujetIndexInline(admin.TabularInline):
	model = ContactSujetIndex

class OrdonnanceInline(admin.TabularInline):
	model = Ordonnance

class PatientResource(resources.ModelResource):
	age = fields.Field(attribute='age')
	class Meta:
		model = Patient
		import_id_fields = ('code_patient',)
		fields=('code_patient', 'presence_soins','sexe', 'date_naissance', 'date_enrolement', 'Date_de_mise_sous_ARV', 'nom_conseiller',)
		export_order=('code_patient', 'presence_soins', 'sexe', 'date_naissance', 'date_enrolement', 'Date_de_mise_sous_ARV','nom_conseiller',)


class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = PatientResource
	list_display = ('code_patient', 'presence_soins', 'sexe', 'date_naissance', 'age', 'date_enrolement', 'Date_de_mise_sous_ARV','nom_conseiller',)
	search_fields=['code_patient',  'nom_prenoms']

	inlines = [
		ChargeViraleInline,
		OrdonnanceInline,
		ContactSujetIndexInline,
	]

admin.site.register(Patient, PatientAdmin,)