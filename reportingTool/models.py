from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import re



# Create your models here.

class Patient(models.Model):

    POST_DE_DEPISTAGE_CHOICES = (
        ('','Choisissez'),
        ('Tuberculose', 'Tuberculose'),
        ('CPN2 et Plus + Acccouch + CPoN', 'CPN2 et Plus + Acccouch + CPoN'),
        ('IST', 'IST'),
        ('Hospitalisation', 'Hospitalisation'),
        ('Index testing','Index testing'),
        ('Urgence','Urgence'),
        ('Malnutrition','Malnutrition'),
        ('Autre CDIP','Autre CDIP')
    )
    post_de_depistage = models.CharField(max_length=30, choices=POST_DE_DEPISTAGE_CHOICES, null=True)


    date_de_depistage = models.DateField(default=date.today ,null=True)

    def code_patient_validate(value):
        reg = re.compile('^[0-9]{4}\/[a-zA-Z0-9]{2}\/[0-9]{2}\/[0-9]{2}\/[0-9]{5}(e|E){0,1}1{0,1}[0-9]{0,1}$')
        if not reg.match(value):
            raise ValidationError(u'%s n\'est pas un code patient valide' % value)
    
    code_patient = models.CharField(max_length=25, validators=[code_patient_validate])

    
    GENDER_CHOICES = (
        ('','Choisissez'),
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    )
    genre = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)


    def age_validate(value):
        if value > 120:
            raise ValidationError(u'%s n\'est pas un âge valide' % value)
    age = models.PositiveSmallIntegerField(validators=[age_validate], null=True)

    # INFORMATION SUR LE TEST DE DÉPISTAGE

    CONSEILLER_CHOICES = (
            ('','Choisissez'),
            ('OUI', 'OUI'),
            ('NON', 'NON'),
        )
    conseiller = models.CharField(max_length=3, choices=CONSEILLER_CHOICES, null=True)


    DEPISTER_CHOICES = (
         ('','Choisissez'),
            ('OUI', 'OUI'),
            ('NON', 'NON'),
        )
    depister = models.CharField(max_length=3, choices=DEPISTER_CHOICES, null=True)


    RESULTAT_TEST_CHOICES = (
        ('','Choisissez'),
        ('Positif', 'Positif'),
        ('Négatif', 'Négatif'),
        ('Indéterminer', 'Indéterminer'),
        ('Statut connu', 'Statut connu')
    )
    resultat = models.CharField(max_length=15, choices=RESULTAT_TEST_CHOICES, null=True)


    RESULTAT_RECU_CHOICES = (
         ('','Choisissez'),      # On veut les conseillés et dépistés ayants reçu leur resultats
            ('OUI', 'OUI'),        # On veut les positifs ayants reçu leur résultat
            ('NON', 'NON'),
        )
    resultat_recu = models.CharField(max_length=3, choices=RESULTAT_RECU_CHOICES, null=True)
     
    

    BENEFICIANT_CD4_CHOICES = ( # Positif bénéficiant d'un CD4 (Seuls les positifs en bénéficient)
         ('','Choisissez'),
            ('OUI', 'OUI'),
            ('NON', 'NON'),
        )
    beneficiant_CD4 = models.CharField(max_length=3, choices=DEPISTER_CHOICES, null=True)
  

    def __str__(self):
        return self.code_patient

