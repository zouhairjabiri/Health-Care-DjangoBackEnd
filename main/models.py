from django.db import models
from multiselectfield import MultiSelectField

##############  CHOICES  ####################

SEXE_CHOICES = (
    ("HOMME", "HOMME"),
    ("FEMME", "FEMME"),
)
STATUS_CHOICES = (
    ("Célibataire", "Célibataire"),
    ("Marié", "Marié"),
    ("Divorcé", "Divorcé"),
    ("Veuf", "Veuf"),
    ("Nonprécisée", "Nonprécisée"),
)

NIVEAU_ETUDE_CHOICES = (
    ("Primaire", "Primaire"),
    ("Collège", "Collège"),
    ("Bac +1 ou +2 ", "Bac +1 ou +2"),
    ("Bac +3 ou +4", "Bac +3 ou +4"),
    ("Bac +5 et plus", "Bac +5 et plus"),
    ("Bac +5 et plus", "Bac +5 et plus"),
    ("Non scolarisé", "Non scolarisé"),
    ("Ecole coranique", "Ecole coranique"),
)
Milieu_de_residence_CHOICES = (
    ("Urbain", "Urbain"),
    ("Rural", "Rural"),
)
Devenirdu_Patient_CHOICES = (
    ("Hospitalisation encours", "Hospitalisation encours"),
    ("Sortie domicile", "Sortie domicile"),
    ("Transfert", "Transfert"),
    ("Décès", "Décès"),

)

Activite_CHOICES = (
    ("élève", "élève"),
    ("étudiant ou en formation ", "étudiant ou en formation"),
    ("Actif", "Actif"),
    ("Retraité", "Retraité"),
    ("Chômeur (ou à la recherche d'un emploi)","Chômeur (ou à la recherche d'un emploi)"),
    ("Femme au foyer", " Femme au foyer"),
    ("Autre, préciser", "Autre, préciser"),
)

Revenu_CHOICES = (
    ("<2500 DH", "<2500 DH"),
    ("[2500 et 5000 DH[", "[2500 et 5000 DH["),
    ("[5000 et 10000 DH[ ", "[5000 et 10000 DH["),
    ("≥10000 DH ", "≥10000 DH "),
    ("Ne sait pas", "Ne sait pas"),
)

TabagismeActif_CHOICES = (
    ("Jamais fumé ", "Jamais fumé "),
    ("Fumeur", "Fumeur"),
    ("Ex-fumeur", "Ex-fumeur"),

)
Symptomes_CHOICES = (
    ("Fièvre", "Fièvre"),
    ("Toux sèche", "Toux sèche"),
    ("Essoufflement", "Essoufflement"),
    ("Dyspnée", "Dyspnée"),
    ("Douleurs musculaires", "Douleurs musculaires"),
    ("Céphalées", "Céphalées"),
    ("Fatigue", "Fatigue"),
    ("Maux de gorge", "Maux de gorge"),
    ("Pharyngite", "Pharyngite"),
    ("Rhinorrhée", "Rhinorrhée"),
    ("Douleur thoracique", "Douleur thoracique"),
    ("Diarrhées", "Diarrhées"),
    ("Nausée", "Nausée"),
    ("Vomissements", "Vomissements"),
    ("Symptomatologie", "Symptomatologie"),
    ("psychiatrique", "psychiatrique"),
    ("Autres, précisez", "Autres, précisez"),
)

ContactPersonne_CHOICES = (
    ("membre de famille", "membre de famille"),
    ("Ami", "Ami"),
    ("Collègue de travail", "Collègue de travail"),
    ("Autre, préciser", "Autre, préciser"),

)
ClassificationSymptomatologique_CHOICES = (
    ("Asymptomatique", "Asymptomatique"),
    ("Symptomatologie clinique de l’infection respiratoire haute (rhinite, pharyngite …)", "Symptomatologie clinique de l’infection respiratoire haute (rhinite, pharyngite …)"),
    ("Symptomatologie clinique de l’infection respiratoire basse (symptômes de pneumonie ou de bronchite…)", "Symptomatologie clinique de l’infection respiratoire basse (symptômes de pneumonie ou de bronchite…)"),
)

##############  class Medicaments  ####################
class Medicaments(models.Model):
    NomMedicament = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Medicament"
        verbose_name_plural = "Medicaments"

    def __str__(self):
        return self.NomMedicament

##############  class HistoireMaladie  ####################
class HistoireMaladie(models.Model):
    NomMaladie = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Histoire Maladie"
        verbose_name_plural = "Histoires Maladies"

    def __str__(self):
        return self.NomMaladie

##############  class Hopital  ####################
class Hopital(models.Model):
    NomHopital = models.CharField(max_length=90)

    class Meta:
        verbose_name = "Hopital"
        verbose_name_plural = "Hopitaux"

    def __str__(self):
        return self.NomHopital

##############  class Comorbidite  ####################
class Comorbidite(models.Model):
    NomAntecedent = models.CharField(max_length=50)

    def __str__(self):
        return self.NomAntecedent




##############  class Doctor  ####################
class Doctor(models.Model):
    Nom = models.CharField(max_length=40)
    Prenom = models.CharField(max_length=40)
    Hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)
    Email = models.EmailField()
    Password = models.CharField(max_length=40)

    def __str__(self):
        return 'Dr.'+self.Nom

##############  class Patient  ####################
class Patient(models.Model):
    Nom = models.CharField(max_length=40)
    Email = models.EmailField()
    Password = models.CharField(max_length=40)
    Prenom = models.CharField(max_length=40)
    DateDeNaissance = models.DateField()
    Sexe = models.CharField(max_length=10, choices=SEXE_CHOICES)
    Statutmatrimonial = models.CharField(max_length=50, choices=STATUS_CHOICES)
    NombreEnfants = models.IntegerField(default=0)
    RevenumMensuel = models.CharField(max_length=40, choices=Revenu_CHOICES)
    NiveauEtude = models.CharField(max_length=40, choices=NIVEAU_ETUDE_CHOICES)
    Activite = models.CharField(max_length=100, choices=Activite_CHOICES, default=Activite_CHOICES[0][0])
    AutreActivite = models.CharField(max_length=100, blank=True)
    Quartier = models.CharField(max_length=50)
    Ville = models.CharField(max_length=40)
    MilieuDeResidence = models.CharField(max_length=10, choices=Milieu_de_residence_CHOICES)
    Poids = models.FloatField()
    Taille = models.FloatField()
    VaccinationBCG = models.BooleanField()
    TabagismeActif = models.CharField(max_length=30, choices=TabagismeActif_CHOICES)
    DureeDeConsommation = models.IntegerField()

    def __str__(self):
        return self.Nom


##############  class ComorbiditePersonnel  ####################
class ComorbiditePersonnel(models.Model):
    Comorbidite = models.ForeignKey(Comorbidite, on_delete=models.CASCADE,blank=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    AgeAuDiagnostic = models.IntegerField(blank=True)
    PriseDeTraitement = models.BooleanField(blank=True)
    AutresMaladies = models.CharField(max_length=90,blank=True)

    def __str__(self):
        return self.Comorbidite.NomAntecedent

##############  class HistoireMaladiePersonnel  ####################
class HistoireMaladiePersonnel(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    HistoireMaladie = models.ForeignKey(HistoireMaladie, on_delete=models.CASCADE)
    Date = models.DateField()
    Specification = models.CharField(max_length=80)

##############  class The National Early Warning Score (NEWS) ####################
class NEWS(models.Model):
    Age = models.FloatField()
    FréquenceRespiratoire = models.FloatField()
    ToutSupplémentOxygène = models.FloatField()
    SaturationOxygène = models.FloatField()
    TA_Systolique = models.FloatField()
    FréquenceCardiaque = models.FloatField()
    Température = models.FloatField()
    NiveauDeConscience = models.FloatField()
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient.Nom


##############  class ContactAvecUnCas  ####################
class ContactAvecUnCas(models.Model):
    ContactConfirme = models.BooleanField()
    ContactPersonne = models.CharField(max_length=40, choices=ContactPersonne_CHOICES)
    AutreContact = models.CharField(max_length=40)
    SourceInconnue = models.BooleanField()
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient.Nom



##############  class ZoneExposition  ####################
class ZoneExposition(models.Model):
    expose = models.BooleanField()
    Zone = models.CharField(max_length=40)
    DateExposition = models.DateField()
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient.Nom


##############  class Enceinte  ####################
class Enceinte(models.Model):
    Grossesse = models.BooleanField()
    NbSemaineamenorrhee = models.IntegerField()
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient.Nom


##############  class StatutClinique  ####################
class StatutClinique(models.Model):
    NomSymptome = MultiSelectField(choices=Symptomes_CHOICES)
    ConclusionExamenClinique = models.CharField(max_length=90)
    ConclusionExamenRadiologique = models.CharField(max_length=40, choices=(("Normale", "Normale"), ("Verre dépoli ", "Verre dépoli ")))
    AutresLesions = models.CharField(max_length=80)
    ClassificationSymptomatologique = models.CharField(max_length=100,choices=ClassificationSymptomatologique_CHOICES)
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    AutresSymptomes = models.CharField(max_length=80)

    def __str__(self):
        return self.NomSymptome

##############  class UtilisationDesMedicaments  ####################
class UtilisationDesMedicaments(models.Model):
    Medicament = models.ForeignKey(Medicaments, on_delete=models.CASCADE,blank=True)
    DureeUtilisation = models.IntegerField(blank=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    AutreMedicaments = models.CharField(max_length=90,blank=True)

    def __str__(self):
        return self.Patient.Nom

##############  class DevenirDuPatient  ####################
class DevenirDuPatient(models.Model):
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    Etat = models.CharField(max_length=90, choices=Devenirdu_Patient_CHOICES)

    def __str__(self):
        return self.Etat

