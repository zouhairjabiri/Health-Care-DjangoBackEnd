from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class MedicamentsViewSet(viewsets.ModelViewSet):
    queryset = Medicaments.objects.all().order_by('id')
    serializer_class = MedicamentsSerializer


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

class UserDocViewSet(viewsets.ModelViewSet):
    queryset = utilisateurDoctor.objects.all().order_by('id')
    serializer_class = UserDocSerializer

    @action(detail=False, methods=['POST'])
    def create_account(self, request):
        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        if utilisateurDoctor.objects.filter(username=username).exists():
            return Response({
                'message': 0
            })
        
        if utilisateurPatient.objects.filter(username=username).exists():
            return Response({
                'message': 0
            })

        try:
            validate_email(username)
        except ValidationError as e:
            return Response({
                'message': 1
            })
        user = utilisateurDoctor.objects.create(
            username=username, first_name=first_name, last_name=last_name, password=password)
        account = UserDocSerializer(user).data
        return Response({
            'id': account['id'],
            'username': account['username'],
            'First_name': account['first_name'],
            'Last_name': account['last_name'],
            'message': True
        })

    @action(detail=False, methods=['POST'])
    def auth_doctor(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            validate_email(username)
        except ValidationError as e:
            return Response({
                'message': 1
            })

        if utilisateurDoctor.objects.filter(username=username,password=password).exists():
            user = utilisateurDoctor.objects.get(username=username,password=password)
            account = UserDocSerializer(user).data
            return Response({
                'id': account['id'],
                'username': account['username'],
                'First_name': account['first_name'],
                'Last_name': account['last_name'],
                'message': True
                })
        return Response({
                'message': 0
            })

class UserPatViewSet(viewsets.ModelViewSet):
    queryset = utilisateurPatient.objects.all().order_by('id')
    serializer_class = UserPatSerializer

    @action(detail=False, methods=['POST'])
    def create_account(self, request):
        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        if utilisateurPatient.objects.filter(username=username).exists():
            return Response({
                'message': 0
            })
        if utilisateurDoctor.objects.filter(username=username).exists():
            return Response({
                'message': 0
            })
            
        try:
            validate_email(username)
        except ValidationError as e:
            return Response({
                'message': 1
            })
        user = utilisateurPatient.objects.create(
            username=username, first_name=first_name, last_name=last_name, password=password)
        account = UserPatSerializer(user).data
        return Response({
            'id': account['id'],
            'username': account['username'],
            'First_name': account['first_name'],
            'Last_name': account['last_name'],
            'message': True
        })

    @action(detail=False, methods=['POST'])
    def auth_patient(self, request):
        username = request.data['username']
        password = request.data['password']

        try:
            validate_email(username)
        except ValidationError as e:
            return Response({
                'message': 1
            })

        if utilisateurPatient.objects.filter(username=username,password=password).exists():
            user = utilisateurPatient.objects.get(username=username,password=password)
            account = UserPatSerializer(user).data
            return Response({
                'id': account['id'],
                'username': account['username'],
                'First_name': account['first_name'],
                'Last_name': account['last_name'],
                'message': True
                })
        return Response({
                'message': 0
            })