from  .models import *
from rest_framework import serializers

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

class ComorbiditePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComorbiditePersonnel
        fields = '__all__'


class HistoireMaladiePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoireMaladiePersonnel
        fields = '__all__'

class utilisateurPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = utilisateurPatient
        fields = ['id', 'first_name', 'last_name', 'username', 'password']

class utilisateurDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = utilisateurDoctor
        fields = ['id', 'first_name', 'last_name', 'username', 'password']
        
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
