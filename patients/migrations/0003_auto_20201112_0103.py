# Generated by Django 3.1.2 on 2020-11-12 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20201109_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_dernier_RDV_ARV',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='date_dernier_RDV_CV',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='date_dernier_RDV_ETP',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='nb_jour_ARV',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='nb_jour_CV',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='nb_jour_ETP',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='resultat_derniere_CV',
        ),
    ]
