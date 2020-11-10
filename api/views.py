from rest_framework import generics

from archivage.models import *
from .serializers import *


class ListDossier(generics.ListCreateAPIView):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer


class DetailDossier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer


class ListAgent(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class DetailAgent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer



class ListMouvement(generics.ListCreateAPIView):
    queryset = Mouvement.objects.all()
    serializer_class = MouvementSerializer


class DetailMouvement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mouvement.objects.all()
    serializer_class = MouvementSerializer


class ListAgentCategory(generics.ListCreateAPIView):
    queryset = AgentCategory.objects.all()
    serializer_class = AgentCategorySerializer


class DetailAgentCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentCategory.objects.all()
    serializer_class = AgentCategorySerializer

