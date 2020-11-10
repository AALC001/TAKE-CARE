from django import forms
from .models import Patient
from datetime import date
import re


class DateInput(forms.DateInput):
    input_type = 'date'

class RptForms(forms.ModelForm):

    class Meta:
        model = Patient

        widget = {'date_de_depistage': DateInput()}

        fields = ('post_de_depistage','date_de_depistage','code_patient', 'genre', 'age', 'conseiller',
         'depister', 'resultat', 'resultat_recu', 'beneficiant_CD4')

        labels = {
            'post_de_depistage': 'Post de dépistage',
            'date_de_depistage': 'Date de dépistage',
            'code_patient':'Code de dépistage',
            'genre':'Sexe',
            'age':'Âge',
            'conseiller':'Conseiller pour le test',
            'depister':'Éffectivement dépisté',
            'resultat':'Résultat du test de dépistage',
            'resultat_recu':'Positif ayant reçu son résultat',
            'beneficiant_CD4':'Positif bénéficiant d\'un CD4'
        }
    
    def __init__(self, *args, **kwargs):
        super(RptForms, self).__init__(*args, **kwargs)
        self.fields['genre'].required = True
        self.fields['conseiller'].required = True
        self.fields['depister'].required = True
        self.fields['resultat'].required = True
        self.fields['resultat_recu'].required = True
        self.fields['beneficiant_CD4'].required = True
        self.fields['post_de_depistage'].required = True
        self.fields['date_de_depistage'].required = True


class RequeteForms(forms.Form):

    date_de_debut = forms.DateField(label='Date de début de la période', widget=DateInput)

    date_de_fin = forms.DateField(label='Date de fin de la période', widget=DateInput)

    region = forms.CharField(label='Région', max_length=50, required=False, initial="ABIDJAN 1 GRAND PONTS")

    district_sanitaire = forms.CharField(label='District Sanitaire', max_length=50, required=False, initial="ADJAME PLATEAU ATTECOUBE")

    etablissement_sanitaire = forms.CharField(label='Établissement Sanitaire', max_length=50, required=False, initial="CSU ABOBO-DOUME")

    code_etablissement_anitaire = forms.CharField(label="Code de l'établissement Sanitaire", max_length=5, required=False)

    code = forms.CharField(label='Code', max_length=50, required=False)

    renseigne_par = forms.CharField(label='Renseigné par', max_length=50, required=False, initial="ReportingTool")


class Filters(forms.Form):

    date_enregistrement = forms.DateField(label="Date d'enregistrement", widget=DateInput, required=False)

    POST_DE_DEPISTAGE_CHOICES = (
        ('Tous','Tous'),
        ('Tuberculose', 'Tuberculose'),
        ('CPN2 et Plus + Acccouch + CPoN', 'CPN2 et Plus + Acccouch + CPoN'),
        ('IST', 'IST'),
        ('Hospitalisation', 'Hospitalisation'),
        ('Index testing','Index testing'),
        ('Urgence','Urgence'),
        ('Malnutrition','Malnutrition'),
        ('Autre CDIP','Autre CDIP')
    )
    post_de_depistage = forms.ChoiceField(choices=POST_DE_DEPISTAGE_CHOICES, label="Post de dépistage", initial='Tous')

    def code_patient_validate(value):
        reg = re.compile('^[0-9]{4}\/[a-zA-Z0-9]{2}\/[0-9]{2}\/[0-9]{2}\/[0-9]{5}(e|E){0,1}1{0,1}[0-9]{0,1}$')
        if not reg.match(value):
            raise ValidationError(u'%s n\'est pas un code patient valide' % value)
    
    code_patient = forms.CharField(max_length=25, validators=[code_patient_validate], required=False)