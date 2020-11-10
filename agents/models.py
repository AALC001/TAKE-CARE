from django.db import models
from django.contrib.auth.models import User
from archivage.models import TimedModel


class AgentCategory(TimedModel):
    title = models.CharField(max_length=50, blank=False, verbose_name="Libelle")
    description = models.CharField(
        'Correspondance sur Slug de state', max_length=200, blank=True, null=True)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Catégorie d'agents"
        verbose_name_plural = "Catégories d'agents"
        ordering = ['title']


class Agent(TimedModel):
    """jhgjgjhgh
    hgj
    dyhthd """
    code = models.CharField(max_length=10, blank=False, unique = True) #,verbose_name="Code agent")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nom = models.CharField(max_length=50, blank=False, verbose_name="NOM")
    prenoms = models.CharField(max_length=50, blank=True, null=True, verbose_name="Prénoms")
    categorie_agent = models.ForeignKey(
        "AgentCategory", on_delete=models.PROTECT, related_name="agents", limit_choices_to={'active': True}, verbose_name="Catégorie")

    @property
    def fullname(self):
        return "{} {}".format(self.prenoms, self.nom.upper())

    def __str__(self):
        return "{} / {} {}".format(self.categorie_agent, self.prenoms, self.nom.upper())

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        ordering = ['code', 'nom', ]