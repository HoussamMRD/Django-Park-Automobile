# Generated by Django 3.0.14 on 2022-04-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicule',
            fields=[
                ('idVh', models.AutoField(primary_key=True, serialize=False)),
                ('matricule', models.CharField(max_length=10)),
                ('marque', models.CharField(max_length=20)),
                ('modele', models.CharField(max_length=20)),
                ('couleur', models.CharField(max_length=20)),
                ('disponible', models.BooleanField()),
            ],
        ),
    ]
