# Generated by Django 3.0.14 on 2022-04-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0002_employe_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='typeCarburant',
            field=models.CharField(choices=[('essence', 'essence'), ('diesel', 'diesel'), ('hybride', 'hybride')], max_length=20, null=True),
        ),
    ]