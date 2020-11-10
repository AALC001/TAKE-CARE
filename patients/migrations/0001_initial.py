# Generated by Django 3.1.2 on 2020-11-08 22:01

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('code_patient', models.CharField(max_length=20, unique=True, verbose_name='Code Patient')),
                ('presence_soins', models.CharField(blank=True, max_length=20, null=True, verbose_name='Présence dans les soins')),
                ('nom_prenoms', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom & Prénom')),
                ('sexe', models.CharField(blank=True, max_length=5, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True, verbose_name='Date de Naissance')),
                ('statut_ARV', models.CharField(blank=True, max_length=5, null=True, verbose_name='Statut ARV')),
                ('date_dernier_RDV_CV', models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2020, 11, 8))], verbose_name='Date dernier RDV CV')),
                ('nb_jour_CV', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Nombre de Jours CV')),
                ('resultat_derniere_CV', models.CharField(blank=True, max_length=50, null=True, verbose_name='resultat derniere CV')),
                ('date_dernier_RDV_ARV', models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2020, 11, 8))], verbose_name='Date de dernier RDV ARV')),
                ('nb_jour_ARV', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Nombre de Jours ARV')),
                ('date_dernier_RDV_ETP', models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2020, 11, 8))], verbose_name='date de dernier RDV ETP')),
                ('nb_jour_ETP', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Nombre de Jours ETP1')),
                ('nom_conseiller', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom et Prénoms du conseiller')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
