from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('Medicaments',views.MedicamentsViewSet)
router.register('Hopital',views.HopitalViewSet)
router.register('Comorbidite',views.ComorbiditeViewSet)
router.register('Doctor',views.DoctorViewSet)
router.register('Patient',views.PatientViewSet)
router.register('ComorbiditePersonnel',views.ComorbiditePersonnelViewSet)
router.register('HistoireMaladiePersonnel',views.HistoireMaladiePersonnelViewSet)
router.register('NEWS',views.NEWSViewSet)
router.register('ContactAvecUnCas',views.ContactAvecUnCasViewSet)
router.register('ZoneExposition',views.ZoneExpositionViewSet)
router.register('Enceinte',views.EnceinteViewSet)
router.register('StatutClinique',views.StatutCliniqueViewSet)
router.register('UtilisationDesMedicaments',views.UtilisationDesMedicamentsViewSet)
router.register('DevenirDuPatient',views.DevenirDuPatientViewSet)
router.register('utilisateurDoctor',views.utilisateurDoctorViewSet)
router.register('utilisateurPatient',views.utilisateurPatientViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = [
   path('', include(router.urls)),
]


