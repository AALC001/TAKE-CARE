# Generated by Django 3.1.2 on 2020-11-03 12:27

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('archivage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DossierOut',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Dossiers hors de la salle d’archivage',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('archivage.dossier',),
        ),
        migrations.CreateModel(
            name='RapportMouvement',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Mouvements de dossiers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('archivage.mouvement',),
        ),
    ]
