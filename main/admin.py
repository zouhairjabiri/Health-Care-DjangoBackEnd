from django.contrib import admin
from .models import *
from .forms import PatientForm

admin.site.site_header = "Télé Covid Administration"
admin.site.site_title = "Télé Covid Administration Portal"
admin.site.index_title = "Bienvenue Dans Télé Covid Portal"


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('Hopital', 'Doctor')
    search_fields = ('utilisateur',)
    list_filter = ('Hopital',)
    fieldsets = (
        ('Informations general', {
            'fields': ('utilisateur', 'Email')
        }),
        ('Hopital ', {
            'fields': ('Hopital',)
        }),
    )

    def Doctor(self, obj):
        return 'Dr. ' + obj.Nom


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Comorbidite)
admin.site.register(Hopital)
admin.site.register(Medicaments)


class ComorbiditePersonnelInline(admin.StackedInline):
    model = ComorbiditePersonnel
    extra = 1


class UtilisationDesMedicamentsInline(admin.StackedInline):
    model = UtilisationDesMedicaments
    extra = 1


class StatutCliniqueInline(admin.StackedInline):
    model = StatutClinique
    extra = 1


class EnceinteInline(admin.StackedInline):
    model = Enceinte
    extra = 1


class ZoneExpositionInline(admin.StackedInline):
    model = ZoneExposition
    extra = 1


class ContactAvecUnCasInline(admin.StackedInline):
    model = ContactAvecUnCas
    extra = 1


class NEWSInline(admin.StackedInline):
    model = NEWS
    extra = 1


class HistoireMaladiePersonnelInline(admin.StackedInline):
    model = HistoireMaladiePersonnel
    extra = 1


class DevenirDuPatientInline(admin.StackedInline):
    model = DevenirDuPatient
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'Sexe', 'devenir')
    search_fields = ('utilisateur', 'Prenom', 'Email', )
    list_filter = ('Sexe',)
    inlines = [
        UtilisationDesMedicamentsInline,
        StatutCliniqueInline,
        EnceinteInline,
        ZoneExpositionInline,
        ContactAvecUnCasInline,
        NEWSInline,
        HistoireMaladiePersonnelInline,
        ComorbiditePersonnelInline,
        DevenirDuPatientInline
    ]
    fieldsets = (
        ('Informations general', {
            'fields': ( 'DateDeNaissance','Sexe', 'NombreEnfants', 'NiveauEtude', 'RevenumMensuel',)
        }),
        ('Activite', {
            'fields': ('Activite',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': ('AutreActivite',),
            'classes': ('abcdefg',)
        }),
        ('Adresse', {
            'fields': ('Quartier', 'Ville', 'MilieuDeResidence',)
        }),
        ('Mesure Physique ', {
            'fields': ('Poids', 'Taille',)
        }),
        ('Vaccination BCG (surtout pour les enfants) ', {
            'fields': ('VaccinationBCG',)
        }),
        ('Tabagisme actif : ', {
            'fields': ('TabagismeActif', 'DureeDeConsommation')
        }),
    )
    form = PatientForm

    def devenir(self, obj):
        devenir = DevenirDuPatient.objects.get(Patient=obj)
        return devenir


admin.site.register(Patient, PatientAdmin)
