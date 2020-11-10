from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RptForms, RequeteForms, Filters
from .models import Patient
from .manipulations import data_traitee, afficher_mois, monthdelta
from .rapport import rapport
from datetime import datetime



# Create your views here.

def home(request):
    return render(request, "reportingTool/home.html")

def rpt_list(request):
    if request.method == "POST":
        print('In POST processing')
        form = Filters(request.POST)

        # RECEUIL DES INFORMATIONS DU FORMULAIRE DE TRIE
        if form.is_valid():

            post_de_depistage = form.cleaned_data['post_de_depistage']
            date_enregistrement = form.cleaned_data['date_enregistrement']
            code_patient = form.cleaned_data['code_patient']

            if code_patient !="":
                patient_list = Patient.objects.filter(code_patient=code_patient)

            elif code_patient=="" and post_de_depistage == "Tous" and date_enregistrement is None:
                patient_list = Patient.objects.all()

            elif code_patient=="" and post_de_depistage == "Tous" and date_enregistrement is not None:
                patient_list = Patient.objects.filter(date_de_depistage=date_enregistrement)

            else:
                patient_list = Patient.objects.filter(date_de_depistage=date_enregistrement).filter(post_de_depistage=post_de_depistage)
            context = {'patient_list': patient_list, 'form': form}
            
        
    else:
        form = Filters()
        context = {'patient_list': Patient.objects.all(), 'form': form}
            
    return render(request, "reportingTool/rpt_list.html", context)

@login_required()
def rpt_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = RptForms()
        else:
            patient = Patient.objects.get(pk=id)
            form = RptForms(instance=patient)
        return render(request, "reportingTool/rpt_form.html", {'form':form})
    
    else:
        if id == 0:
            form = RptForms(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = RptForms(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        else:
            return redirect('patient_insert')

def rpt_delete(request, id):
    patient = Patient.objects.get(pk=id)
    patient.delete()
    return redirect('patient_list')


# Authentification

#def loginView(request):
#    return render(request, "reportingTool/login.html")

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "reportingTool/register.html", {'form': form})


#Rapportage
def reportView(request): 
    if request.method == "POST":
        print('In POST processing')
        form = RequeteForms(request.POST)

        # RECEUIL DES INFORMATIONS DU FORMULAIRE DE RAPPORTAGE
        if form.is_valid():

            date_debut = form.cleaned_data['date_de_debut']
            date_fin = form.cleaned_data['date_de_fin']
            region = form.cleaned_data['region']
            district_sanitaire = form.cleaned_data['district_sanitaire']
            etablissement_sanitaire = form.cleaned_data['etablissement_sanitaire']
            code_etablissement_anitaire = form.cleaned_data['code_etablissement_anitaire']
            code = form.cleaned_data['code']
            renseigne_par = form.cleaned_data['renseigne_par']

            annee = date_fin.strftime("%Y")

            # Affichage du mois de rapportage
            delta = monthdelta(date_debut,date_fin)
            if delta == 1:
                mois = afficher_mois(int(date_debut.strftime("%m")))
            elif delta == 3:
                cle = int(date_debut.strftime("%m"))
                mois = afficher_mois(cle)+" - " + afficher_mois((cle + 1) % 12) + " - " + afficher_mois((cle + 2) % 12)
            date_remplissage = datetime.now().strftime("%d/%m/%Y")



            # CREATION DES DONNÉES D'ANALYSE
            donnee = Patient.objects.filter(date_de_depistage__gte=date_debut).filter(date_de_depistage__lte=date_fin)
            donnee = donnee.values("post_de_depistage","genre", "age","conseiller","depister","resultat","resultat_recu", "beneficiant_CD4")
            donnee = list(donnee)
            donnee = data_traitee(donnee)

            # CREATION DES LIBÉLLÉ DU RAPPORT
            libelle={
                "Mois :":mois,
                "region :":region,
                "District Sanitaire : ":district_sanitaire,
                "Etablissement Sanitaire :":etablissement_sanitaire,
                "Code de l'établissement Sanitaire : ":code_etablissement_anitaire,
                "Année :":annee,
                "Code :":code,
                "Renseigné par :": renseigne_par,
                "Date de remplissage :":date_remplissage
            }
            # NOM DU FICHIER DE RAPPORTAGE
            nom_fichier = "CANEVAS DONNEES COMPLEMENTAIRES " + libelle["Mois :"].upper() + " " + libelle["Année :"] + " " + libelle["Etablissement Sanitaire :"].upper()
            rapport(donnee, libelle, nom_fichier)
            
            return redirect('patient_list')
    else:
        form = RequeteForms()
        return render(request, "reportingTool/report.html", {'form': form})