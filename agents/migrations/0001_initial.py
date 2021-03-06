# Generated by Django 3.1.2 on 2020-10-31 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('title', models.CharField(max_length=50, verbose_name='Libelle')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Correspondance sur Slug de state')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': "Catégorie d'agents",
                'verbose_name_plural': "Catégories d'agents",
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('code', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=50, verbose_name='NOM')),
                ('prenoms', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prénoms')),
                ('categorie_agent', models.ForeignKey(limit_choices_to={'active': True}, on_delete=django.db.models.deletion.PROTECT, related_name='agents', to='agents.agentcategory', verbose_name='Catégorie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
                'ordering': ['code', 'nom'],
            },
        ),
    ]
