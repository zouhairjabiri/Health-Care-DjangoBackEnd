from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = utilisateurDoctor
        fields = ['id', 'first_name', 'last_name', 'username', 'password']
        required_fields = fields
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            },
        }

class UserPatSerializer(serializers.ModelSerializer):
    class Meta:
        model = utilisateurPatient
        fields = ['id', 'first_name', 'last_name', 'username', 'password']
        required_fields = fields
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            },
        }


class MedicamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicaments
        fields = '__all__'

class HopitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hopital
        fields = '__all__'

class ComorbiditeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comorbidite
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  

    def to_representation(self, instance):
        self.fields['utilisateur'] = UserPatSerializer(read_only=True)
        return super(PatientSerializer, self).to_representation(instance) 

class ComorbiditePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComorbiditePersonnel
        fields = '__all__'


class HistoireMaladiePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoireMaladiePersonnel
        fields = '__all__'

     
class NEWSSerializer(serializers.ModelSerializer):
    class Meta:
        model = NEWS
        fields = '__all__'
class ContactAvecUnCasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAvecUnCas
        fields = '__all__'

class ZoneExpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneExposition
        fields = '__all__'

class EnceinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enceinte
        fields = '__all__' 



class StatutCliniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutClinique
        fields = '__all__' 

class UtilisationDesMedicamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilisationDesMedicaments
        fields = '__all__'   

class DevenirDuPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevenirDuPatient
        fields = '__all__'  




