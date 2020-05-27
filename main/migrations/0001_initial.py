# Generated by Django 3.0.3 on 2020-05-27 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comorbidite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomAntecedent', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HistoireMaladie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomMaladie', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Histoire Maladie',
                'verbose_name_plural': 'Histoires Maladies',
            },
        ),
        migrations.CreateModel(
            name='Hopital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomHopital', models.CharField(max_length=90)),
            ],
            options={
                'verbose_name': 'Hopital',
                'verbose_name_plural': 'Hopitaux',
            },
        ),
        migrations.CreateModel(
            name='Medicaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomMedicament', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Medicament',
                'verbose_name_plural': 'Medicaments',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=40)),
                ('Prenom', models.CharField(max_length=40)),
                ('DateDeNaissance', models.DateField()),
                ('Sexe', models.CharField(choices=[('HOMME', 'HOMME'), ('FEMME', 'FEMME')], max_length=10)),
                ('Statutmatrimonial', models.CharField(choices=[('Célibataire', 'Célibataire'), ('Marié', 'Marié'), ('Divorcé', 'Divorcé'), ('Veuf', 'Veuf'), ('Nonprécisée', 'Nonprécisée')], max_length=50)),
                ('NombreEnfants', models.IntegerField(default=0)),
                ('RevenumMensuel', models.CharField(choices=[('<2500 DH', '<2500 DH'), ('[2500 et 5000 DH[', '[2500 et 5000 DH['), ('[5000 et 10000 DH[ ', '[5000 et 10000 DH['), ('≥10000 DH ', '≥10000 DH '), ('Ne sait pas', 'Ne sait pas')], max_length=40)),
                ('NiveauEtude', models.CharField(choices=[('Primaire', 'Primaire'), ('Collège', 'Collège'), ('Bac +1 ou +2 ', 'Bac +1 ou +2'), ('Bac +3 ou +4', 'Bac +3 ou +4'), ('Bac +5 et plus', 'Bac +5 et plus'), ('Bac +5 et plus', 'Bac +5 et plus'), ('Non scolarisé', 'Non scolarisé'), ('Ecole coranique', 'Ecole coranique')], max_length=40)),
                ('Activite', models.CharField(choices=[('élève', 'élève'), ('étudiant ou en formation ', 'étudiant ou en formation'), ('Actif', 'Actif'), ('Retraité', 'Retraité'), ("Chômeur (ou à la recherche d'un emploi)", "Chômeur (ou à la recherche d'un emploi)"), ('Femme au foyer', ' Femme au foyer'), ('Autre, préciser', 'Autre, préciser')], default='élève', max_length=100)),
                ('AutreActivite', models.CharField(blank=True, max_length=100)),
                ('Quartier', models.CharField(max_length=50)),
                ('Ville', models.CharField(max_length=40)),
                ('MilieuDeResidence', models.CharField(choices=[('Urbain', 'Urbain'), ('Rural', 'Rural')], max_length=10)),
                ('Poids', models.FloatField()),
                ('Taille', models.FloatField()),
                ('VaccinationBCG', models.BooleanField()),
                ('TabagismeActif', models.CharField(choices=[('Jamais fumé ', 'Jamais fumé '), ('Fumeur', 'Fumeur'), ('Ex-fumeur', 'Ex-fumeur')], max_length=30)),
                ('DureeDeConsommation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ZoneExposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expose', models.BooleanField()),
                ('Zone', models.CharField(max_length=40)),
                ('DateExposition', models.DateField()),
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='UtilisationDesMedicaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DureeUtilisation', models.IntegerField(blank=True)),
                ('AutreMedicaments', models.CharField(blank=True, max_length=90)),
                ('Medicament', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Medicaments')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='StatutClinique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomSymptome', models.CharField(choices=[('Fièvre', 'Fièvre'), ('Toux sèche', 'Toux sèche'), ('Essoufflement', 'Essoufflement'), ('Dyspnée', 'Dyspnée'), ('Douleurs musculaires', 'Douleurs musculaires'), ('Céphalées', 'Céphalées'), ('Fatigue', 'Fatigue'), ('Maux de gorge', 'Maux de gorge'), ('Pharyngite', 'Pharyngite'), ('Rhinorrhée', 'Rhinorrhée'), ('Douleur thoracique', 'Douleur thoracique'), ('Diarrhées', 'Diarrhées'), ('Nausée', 'Nausée'), ('Vomissements', 'Vomissements'), ('Symptomatologie', 'Symptomatologie'), ('psychiatrique', 'psychiatrique'), ('Autres, précisez', 'Autres, précisez')], max_length=40)),
                ('AutresSymptomes', models.CharField(max_length=80)),
                ('ConclusionExamenClinique', models.CharField(max_length=90)),
                ('ConclusionExamenRadiologique', models.CharField(choices=[('Normale', 'Normale'), ('Verre dépoli ', 'Verre dépoli ')], max_length=40)),
                ('AutresLesions', models.CharField(max_length=80)),
                ('ClassificationSymptomatologique', models.CharField(choices=[('Asymptomatique', 'Asymptomatique'), ('Symptomatologie clinique de l’infection respiratoire haute (rhinite, pharyngite …)', 'Symptomatologie clinique de l’infection respiratoire haute (rhinite, pharyngite …)'), ('Symptomatologie clinique de l’infection respiratoire basse (symptômes de pneumonie ou de bronchite…)', 'Symptomatologie clinique de l’infection respiratoire basse (symptômes de pneumonie ou de bronchite…)')], max_length=100)),
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='NEWS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.FloatField()),
                ('FréquenceRespiratoire', models.FloatField()),
                ('ToutSupplémentOxygène', models.FloatField()),
                ('SaturationOxygène', models.FloatField()),
                ('TA_Systolique', models.FloatField()),
                ('FréquenceCardiaque', models.FloatField()),
                ('Température', models.FloatField()),
                ('NiveauDeConscience', models.FloatField()),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='HistoireMaladiePersonnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Specification', models.CharField(max_length=80)),
                ('HistoireMaladie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.HistoireMaladie')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Enceinte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grossesse', models.BooleanField()),
                ('NbSemaineamenorrhee', models.IntegerField()),
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=40)),
                ('Prenom', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=40)),
                ('Hopital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Hopital')),
            ],
        ),
        migrations.CreateModel(
            name='DevenirDuPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Etat', models.CharField(choices=[('Hospitalisation encours', 'Hospitalisation encours'), ('Sortie domicile', 'Sortie domicile'), ('Transfert', 'Transfert'), ('Décès', 'Décès')], max_length=90)),
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ContactAvecUnCas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactConfirme', models.BooleanField()),
                ('ContactPersonne', models.CharField(choices=[('membre de famille', 'membre de famille'), ('Ami', 'Ami'), ('Collègue de travail', 'Collègue de travail'), ('Autre, préciser', 'Autre, préciser')], max_length=40)),
                ('AutreContact', models.CharField(max_length=40)),
                ('SourceInconnue', models.BooleanField()),
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ComorbiditePersonnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AgeAuDiagnostic', models.IntegerField(blank=True)),
                ('PriseDeTraitement', models.BooleanField(blank=True)),
                ('AutresMaladies', models.CharField(blank=True, max_length=90)),
                ('Comorbidite', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Comorbidite')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
    ]