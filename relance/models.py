import datetime
#from dateutil import relativedelta
from datetime import timedelta
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator
from patients.models import Patient
# Create your models here.

class TimedModel(models.Model):

	creation_time = models.DateTimeField(auto_now_add=True, verbose_name="Date de creation")
	update_time = models.DateTimeField(auto_now=True, verbose_name="Date de modification")

	class Meta:
		abstract = True

class RendezVous(TimedModel):
	code_patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="rendez_vous")
	date_dernier_RDV_CV = models.DateField('Date dernier RDV CV', blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	resultat_derniere_CV= models.CharField("resultat derniere CV", max_length=50, blank=True, null=True)
	nb_jour_CV = models.PositiveIntegerField("Nombre de Jours avant la prochaine CV", default = 0, blank=True, null=True)
	date_dernier_RDV_ARV = models.DateField("Date de dernier RDV ARV", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	nb_jour_ARV = models.PositiveIntegerField("Nombre de Jours ARV", default = 0, blank=True, null=True)
	date_dernier_RDV_ETP = models.DateField('date de dernier RDV ETP', blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	nb_jour_ETP = models.PositiveIntegerField("Nombre de Jours ETP1", default = 0, blank=True, null=True)

	class Meta:
		verbose_name = "Gestion des Rendez-Vous"
		verbose_name_plural = "Gestion des Rendez-Vous"
	
	@property
	def presence_en_soins(self):
		return self.code_patient.presence_soins
	
	@property
	def nom_et_prenoms(self):
		return self.code_patient.nom_prenoms
	
	@property
	def sexe(self):
		return self.code_patient.sexe
	
	@property
	def nom_conseiller(self):
		return self.code_patient.nom_conseiller


class ProchainRendezVous(TimedModel):
	code_patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="prochains_rdv")
	rdv = models.ForeignKey("RendezVous", on_delete=models.CASCADE, blank=True, null=True, related_name="prochains_rdv" , editable=False)

	class Meta:
		verbose_name = "Date Prévu Prochains Rendez-Vous"
		verbose_name_plural = "Dates Prévus Prochains Rendez-Vous"

	@property
	def date_prochain_rdv_CV(self):
		date1 = self.rdv.date_dernier_RDV_CV
		if self.rdv.nb_jour_CV is None:
			return date1
		else:
			date2 = datetime.timedelta(days=self.rdv.nb_jour_CV - 5)
			return date1 + date2
	
	@property
	def rdv_CV_manque(self):
		if str(self.date_prochain_rdv_CV) < str(datetime.datetime.now()):
			return self.date_prochain_rdv_CV
		else:
			return "----"

	@property
	def date_prochain_rdv_ETP(self):
		date1 = self.rdv.date_dernier_RDV_ETP
		if self.rdv.nb_jour_ETP is None:
			return date1
		else:
			date2 = datetime.timedelta(days=self.rdv.nb_jour_ETP - 5)
			return date1 + date2
	
	@property
	def rdv_ETP_manque(self):
		if str(self.date_prochain_rdv_ETP) < str(datetime.datetime.now()):
			return self.date_prochain_rdv_ETP
		else:
			return "----"

	@property
	def date_prochain_rdv_ARV(self):
		date1 = self.rdv.date_dernier_RDV_ARV
		if self.rdv.nb_jour_ARV is None:
			return date1
		else:
			date2 = datetime.timedelta(days=self.rdv.nb_jour_ARV - 5)
			return date1 + date2

	@property
	def rdv_ARV_manque(self):
		if str(self.date_prochain_rdv_ARV) < str(datetime.datetime.now()):
			return self.date_prochain_rdv_ARV
		else:
			return "----"

	@property
	def presence_en_soins(self):
		return self.code_patient.presence_soins
	
	@property
	def nom_et_prenoms(self):
		return self.code_patient.nom_prenoms
	
	@property
	def sexe(self):
		return self.code_patient.sexe
	
	@property
	def nom_conseiller(self):
		return self.code_patient.nom_conseiller
	
	

	#@property
	#def statut_RDV(self):
	#	if str(self.derniere_relance) < str(self.derniere_visite):
	#		return "patients_venus"
	#	else :
	#		return "patients_non_venus"
	#@property
	#def passassion(self):
	#	date1 = datetime.timedelta(days=92)
	#	date2 = self.date + date1
	#	if str(datetime.datetime.now()) > str(date2) :
	#		return "A remettre aux conseillères communautaires"
	#	else:
	#		return "En vigueur"

class SuiviRdvARV(TimedModel):
	code_patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="suivi_rdv_arv")
	#date_rdv = models.DateField("Date de RDV", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	type_visite = models.CharField("Type de Visite",max_length=20, blank=True, null=True)
	date_rappel = models.DateField("Date de Rappel", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	methode_rappel = models.CharField("Méthode de rappel",max_length=20, blank=True, null=True)
	feedback_rappel = models.CharField("Feedback rappel",max_length=50, blank=True, null=True)
	date_derniere_relance = models.DateField("Date de dernière relance", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	methode_derniere_relance = models.CharField("Méthode de dernière relance",max_length=20, blank=True, null=True)
	feedback_derniere_relance = models.CharField("feedback de la dernière relance",max_length=50, blank=True, null=True)

	class Meta:
		verbose_name = "Suivi des RDV ARV"
		verbose_name_plural = "Suivi des RDV ARV"
	
	@property
	def presence_en_soins(self):
		return self.code_patient.presence_soins
	
	@property
	def nom_et_prenoms(self):
		return self.code_patient.nom_prenoms
	
	@property
	def sexe(self):
		return self.code_patient.sexe

	@property
	def nom_du_conseiller(self):
		return self.code_patient.nom_conseiller

	@property
	def date_prochain_rdv_ARV(self):
		date1 = self.code_patient.date_dernier_RDV_ARV
		if self.code_patient.nb_jour_ARV is None:
			return date1
		else:
			date2 = datetime.timedelta(days=self.code_patient.nb_jour_ARV - 5)
			return date1 + date2


class SuiviRdvCV(TimedModel):
	code_patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="suivi_rdv_cv")
	#date_rdv = models.DateField("Date de RDV", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	type_visite = models.CharField("Type de Visite",max_length=20, blank=True, null=True)
	date_rappel = models.DateField("Date de Rappel", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	methode_rappel = models.CharField("Méthode de rappel",max_length=20, blank=True, null=True)
	feedback_rappel = models.CharField("Feedback rappel",max_length=50, blank=True, null=True)
	date_derniere_relance = models.DateField("Date de dernière relance", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	methode_derniere_relance = models.CharField("Méthode de dernière relance",max_length=20, blank=True, null=True)
	feedback_derniere_relance = models.CharField("feedback de la dernière relance",max_length=50, blank=True, null=True)

	class Meta:
		verbose_name = "Suivi des RDV CV"
		verbose_name_plural = "Suivi des RDV CV"
	
	@property
	def presence_en_soins(self):
		return self.code_patient.presence_soins
	
	@property
	def nom_et_prenoms(self):
		return self.code_patient.nom_prenoms
	
	@property
	def sexe(self):
		return self.code_patient.sexe

	@property
	def nom_du_conseiller(self):
		return self.code_patient.nom_conseiller

	@property
	def date_prochain_rdv_CV(self):
		date1 = self.code_patient.date_dernier_RDV_CV
		if self.code_patient.nb_jour_CV is None:
			return date1
		else:
			date2 = datetime.timedelta(days=self.code_patient.nb_jour_CV - 5)
			return date1 + date2


class ContactSujetIndex(TimedModel):
	code_patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="contact_sujet_index")
	code_contact = models.CharField("Code du sujet contact",max_length=30, blank=True, null=True, unique=True)
	nature_lien = models.CharField("Nature du lien avec le sujet index",max_length=20, blank=True, null=True,)
	sexe = models.CharField("Sexe du contact",max_length=5, blank=True, null=True,)
	date_naissance = models.DateField("Date de naissance",blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	statut_identification = models.CharField("Statut à l'identification",max_length=20, blank=True, null=True,)
	date_depistage = models.DateField("Date de dépistage",blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	resultat_depistage = models.CharField("Résultat de dépistage",max_length=30, blank=True, null=True,)

	class Meta:
		verbose_name = "Contact du sujet Index"
		verbose_name_plural = "Contacts du sujet Index"
	
	@property
	def presence_en_soins(self):
		return self.code_patient.presence_soins
	
	@property
	def nom_et_prenoms(self):
		return self.code_patient.nom_prenoms
	
	@property
	def sexe_patient(self):
		return self.code_patient.sexe
	
	@property
	def nom_du_conseiller(self):
		return self.code_patient.nom_conseiller


