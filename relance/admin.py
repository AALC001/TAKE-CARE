from django.contrib import admin
from .models import *
import datetime
from datetime import timedelta
from django.utils import timezone
from reversion.admin import VersionAdmin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export import resources,fields,widgets

from patients.models import Patient



class RendezVousResource(resources.ModelResource):
	rdv_ARV_manque = fields.Field(attribute='rdv_ARV_manque')
	rdv_CV_manque = fields.Field(attribute='rdv_CV_manque')
	rdv_ETP_manque = fields.Field(attribute='rdv_ETP_manque')

	class Meta:
		model=RendezVous
		import_id_fields=('code_patient',)
		fields=('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe',
		'date_dernier_RDV_CV','resultat_derniere_CV','nb_jour_CV' ,'date_dernier_RDV_ARV', 'nb_jour_ARV','date_dernier_RDV_ETP','nb_jour_ETP',
		'code_patient__nom_conseiller',)

		export_order = ('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe',)

class RendezVousAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = RendezVousResource
	list_display = ('code_patient', 'presence_en_soins', 'nom_et_prenoms','sexe',
	'date_dernier_RDV_CV','resultat_derniere_CV','nb_jour_CV' ,'date_dernier_RDV_ARV', 'nb_jour_ARV','date_dernier_RDV_ETP','nb_jour_ETP',
	'nom_conseiller',)
	#'date_rdv_ETP2', 'date_rdv_ETP3',
	#list_filter = ('categorie','BUT_RDV')

class ProchainRendezVousResource(resources.ModelResource):
	rdv_ARV_manque = fields.Field(attribute='rdv_ARV_manque')
	rdv_CV_manque = fields.Field(attribute='rdv_CV_manque')
	rdv_ETP_manque = fields.Field(attribute='rdv_ETP_manque')
	class Meta:
		model=ProchainRendezVous
		import_id_fields=('code_patient',)
		fields=('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe',
		'date_prochain_rdv_ARV','date_prochain_rdv_CV', 'date_prochain_rdv_ETP','code_patient__nom_conseiller',)

		export_order = ('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe',)

class ProchainRendezVousAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = ProchainRendezVousResource
	list_display = ('code_patient', 'presence_en_soins', 'nom_et_prenoms','sexe',
	'date_prochain_rdv_ARV','date_prochain_rdv_CV', 'date_prochain_rdv_ETP','nom_conseiller',)
	#'date_rdv_ETP2', 'date_rdv_ETP3',
	#list_filter = ('categorie','BUT_RDV')

class RendezVousManque(ProchainRendezVous):
	class Meta:
		proxy = True
		verbose_name_plural = "Rendez-Vous Manqués"

class RendezVousManqueAdmin(ProchainRendezVousAdmin):
	list_display = ['code_patient','presence_en_soins','nom_et_prenoms','sexe','rdv_ARV_manque','rdv_CV_manque','rdv_ETP_manque']


class SuiviRdvARVResource(resources.ModelResource):
	date_prochain_rdv_ARV = fields.Field(attribute='date_prochain_rdv_ARV')
	class Meta:
		model = SuiviRdvARV
		import_id_fields = ('code_patient',)
		fields=('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe', 'date_prochain_rdv_ARV','type_visite',
		'date_rappel','methode_rappel','feedback_rappel','date_derniere_relance','methode_derniere_relance','feedback_derniere_relance','nom_du_conseiller',)

@admin.register(SuiviRdvARV)
class SuiviRdvARVAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = SuiviRdvARVResource
	list_display = ('code_patient', 'presence_en_soins', 'nom_et_prenoms','sexe', 'date_prochain_rdv_ARV', 'type_visite','date_rappel',
	'methode_rappel','feedback_rappel','date_derniere_relance','methode_derniere_relance','feedback_derniere_relance','nom_du_conseiller',)

class SuiviRdvCVResource(resources.ModelResource):
	date_prochain_rdv_CV = fields.Field(attribute='date_prochain_rdv_CV')
	class Meta:
		model = SuiviRdvCV
		import_id_fields = ('code_patient',)
		fields=('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe', 'date_prochain_rdv_CV','type_visite',
		'date_rappel','methode_rappel','feedback_rappel','date_derniere_relance','methode_derniere_relance','feedback_derniere_relance','nom_du_conseiller',)


@admin.register(SuiviRdvCV)
class SuiviRdvARVAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = SuiviRdvCVResource
	list_display = ('code_patient', 'presence_en_soins', 'nom_et_prenoms','sexe', 'date_prochain_rdv_CV','type_visite','date_rappel',
	'methode_rappel','feedback_rappel','date_derniere_relance','methode_derniere_relance','feedback_derniere_relance','nom_du_conseiller',)

class ContactSujetIndexResource(resources.ModelResource):
	class Meta:
		model = ContactSujetIndex
		import_id_fields = ('code_patient',)
		fields=('code_patient', 'code_patient__presence_soins', 'code_patient__nom_prenoms','code_patient__sexe', 'code_contact','nature_lien','sexe',
		'date_naissance','statut_identification','date_depistage','resultat_depistage','nom_du_conseiller',)

@admin.register(ContactSujetIndex)
class ContactSujetIndexAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = ContactSujetIndexResource
	list_display = ('code_patient', 'presence_en_soins', 'nom_et_prenoms','sexe', 'code_contact', 'nature_lien','sexe_patient','date_naissance',
	'statut_identification','date_depistage','resultat_depistage','nom_du_conseiller',)

admin.site.register(ProchainRendezVous, ProchainRendezVousAdmin)
admin.site.register(RendezVousManque, RendezVousManqueAdmin)
admin.site.register(RendezVous, RendezVousAdmin)