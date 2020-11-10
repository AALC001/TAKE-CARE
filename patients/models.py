from django.db import models
from archivage.models import TimedModel
import datetime
#from dateutil import relativedelta
from datetime import timedelta
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.

class Patient(TimedModel):
	code_patient = models.CharField("Code Patient",max_length=20, blank=False, unique=True)
	presence_soins = models.CharField("Présence dans les soins",max_length=20, blank=True, null=True)
	nom_prenoms = models.CharField("Nom & Prénom",max_length=50, blank=True, null=True)
	sexe = models.CharField(max_length=5, blank=True, null=True)
	date_naissance = models.DateField("Date de Naissance", blank=True, null=True)
	statut_ARV = models.CharField("Statut ARV",max_length=5, blank=True, null=True)
	date_dernier_RDV_CV = models.DateField('Date dernier RDV CV', blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	nb_jour_CV = models.PositiveIntegerField("Nombre de Jours CV", default = 0, blank=True, null=True)
	resultat_derniere_CV= models.CharField("resultat derniere CV",max_length=50, blank=True, null=True)
	date_dernier_RDV_ARV = models.DateField("Date de dernier RDV ARV", blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	nb_jour_ARV = models.PositiveIntegerField("Nombre de Jours ARV", default = 0, blank=True, null=True)
	date_dernier_RDV_ETP = models.DateField('date de dernier RDV ETP', blank=True, null=True, validators = [MaxValueValidator(datetime.datetime.now().date())])
	nb_jour_ETP = models.PositiveIntegerField("Nombre de Jours ETP1", default = 0, blank=True, null=True)
	nom_conseiller = models.CharField("Nom et Prénoms du conseiller",max_length=50, blank=True, null=True)

	def __str__(self):
		return self.code_patient

	@property
	def age(self):
		if self.date_naissance is None:
			return None
		else:
			return int(datetime.datetime.now().year) - int(self.date_naissance.year)

	#@property
	#def cohorte_actuelle(self):
	#	if self.Date_de_mise_sous_ARV is None:
	#		return '0'
	#	else:
	#		today = datetime.datetime.now()
	#		diff_mois = (today.year - self.Date_de_mise_sous_ARV.year) *12 + today.month - self.Date_de_mise_sous_ARV.month + 1
	#		return "M{}".format(str(diff_mois))