# Generated by Django 3.0.14 on 2022-04-21 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employe',
            fields=[
                ('idEm', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('permis', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='mission',
            fields=[
                ('idM', models.AutoField(primary_key=True, serialize=False)),
                ('typeM', models.CharField(max_length=20)),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('lieuDepart', models.CharField(max_length=20)),
                ('lieuArrivee', models.CharField(max_length=20)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.employe')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.vehicule')),
            ],
        ),
    ]
