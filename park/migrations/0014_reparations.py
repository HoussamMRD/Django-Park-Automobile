# Generated by Django 3.0.14 on 2022-05-27 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0013_remove_location_prix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_Panne', models.CharField(choices=[('batterie', ' batterie'), ('fuite du joint de culasse', 'fuite du joint de culasse'), (' l’huile moteur', ' l’huile moteur'), (' liquide de refroidissement', ' liquide de refroidissement')], max_length=100, null=True)),
                ('date_Rep', models.DateTimeField(null=True)),
                ('desc_Rep', models.CharField(max_length=500)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.vehicule')),
            ],
        ),
    ]