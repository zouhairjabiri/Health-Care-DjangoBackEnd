from rest_framework import viewsets
from .serializers import *
from .models import *

class MedicamentsViewSet(viewsets.ModelViewSet):
    queryset = Medicaments.objects.all().order_by('id')
    serializer_class = MedicamentsSerializer

class utilisateurDoctorViewSet(viewsets.ModelViewSet):
    queryset = utilisateurDoctor.objects.all().order_by('id')
    serializer_class = utilisateurDoctorSerializer

class utilisateurPatientViewSet(viewsets.ModelViewSet):
    queryset = utilisateurPatient.objects.all().order_by('id')
    serializer_class = utilisateurPatientSerializer


class HopitalViewSet(viewsets.ModelViewSet):
    queryset = Hopital.objects.all().order_by('id')
    serializer_class = HopitalSerializer


class ComorbiditeViewSet(viewsets.ModelViewSet):
    queryset = Comorbidite.objects.all().order_by('id')
    serializer_class = ComorbiditeSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer


class ComorbiditePersonnelViewSet(viewsets.ModelViewSet):
    queryset = ComorbiditePersonnel.objects.all().order_by('id')
    serializer_class = ComorbiditePersonnelSerializer


class HistoireMaladiePersonnelViewSet(viewsets.ModelViewSet):
    queryset = HistoireMaladiePersonnel.objects.all().order_by('id')
    serializer_class = HistoireMaladiePersonnelSerializer


class NEWSViewSet(viewsets.ModelViewSet):
    queryset = NEWS.objects.all().order_by('id')
    serializer_class = NEWSSerializer


class ContactAvecUnCasViewSet(viewsets.ModelViewSet):
    queryset = ContactAvecUnCas.objects.all().order_by('id')
    serializer_class = ContactAvecUnCasSerializer


class ZoneExpositionViewSet(viewsets.ModelViewSet):
    queryset = ZoneExposition.objects.all().order_by('id')
    serializer_class = ZoneExpositionSerializer


class EnceinteViewSet(viewsets.ModelViewSet):
    queryset = Enceinte.objects.all().order_by('id')
    serializer_class = EnceinteSerializer


class StatutCliniqueViewSet(viewsets.ModelViewSet):
    queryset = StatutClinique.objects.all().order_by('id')
    serializer_class = StatutCliniqueSerializer


class UtilisationDesMedicamentsViewSet(viewsets.ModelViewSet):
    queryset = UtilisationDesMedicaments.objects.all().order_by('id')
    serializer_class = UtilisationDesMedicamentsSerializer


class DevenirDuPatientViewSet(viewsets.ModelViewSet):
    queryset = DevenirDuPatient.objects.all().order_by('id')
    serializer_class = DevenirDuPatientSerializer
