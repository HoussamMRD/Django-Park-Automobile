from queue import LifoQueue
from unicodedata import category
from django.db import models





class vehicule(models.Model):
    idVh = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=10)
    marque = models.CharField(max_length=20)
    modele = models.CharField(max_length=20)
    couleur = models.CharField(max_length=20)
    Availability = models.CharField(max_length=20,null=True,choices=[('Dispo','Dispo'),('DuringMiss','DuringMiss'),('enPanne','enPanne')])
    typeCarburant = models.CharField(max_length=20,null=True,choices=[('essence','essence'),('diesel','diesel'),('hybride','hybride')])
    Status = models.CharField(max_length=20,null=True,choices=[('Aprov','Aprov'),('Reject','Reject')])
    def __str__(self):
        return self.marque


class employe(models.Model):
    idEm = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    NumPermis = models.CharField(max_length=20,null=True)
    category_Permis = models.CharField(max_length=20,null=True)
    date_EXP_Permis = models.DateField(null=True)
    telephone = models.CharField(max_length=20)
    disponibilite = models.CharField(max_length=20,null=True,choices=[('Dispo','Dispo'),('DuringMiss','DuringMiss'),('NonDispo','NonDispo')])
    def __str__(self):
        return self.nom


class mission(models.Model):
    idM = models.AutoField(primary_key=True)
    typeM = models.CharField(max_length=20)
    StartMiss=models.DateTimeField(null=True)
    EndMiss=models.DateTimeField(null=True)
    lieuDepart = models.CharField(max_length=20)
    lieuArrivee = models.CharField(max_length=20)
    vehicule = models.ForeignKey(vehicule, on_delete=models.CASCADE)
    employe = models.ForeignKey(employe, on_delete=models.CASCADE)
    def __str__(self):
        return self.typeM






class Question(models.Model):
    employe= models.ForeignKey(employe, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description




class Location(models.Model):
    vehicule= models.ForeignKey(vehicule, on_delete=models.CASCADE)
    type_Location=models.CharField(max_length=20,null=True,choices=[('Achat','Achat'),('Rent','Rent'),('Credit','Credit')])
    Start_Location=models.DateTimeField(null=True)
    End_Location=models.DateTimeField(null=True)
    def __str__(self):
        return self.type_Location



class Reparation(models.Model):
    vehicule= models.ForeignKey(vehicule, on_delete=models.CASCADE)
    type_Panne=models.CharField(max_length=100,null=True,choices=[( 'vidange','vidange'),( 'batterie',' batterie'),('fuite du joint de culasse','fuite du joint de culasse'),(' l’huile moteur',' l’huile moteur'),(' liquide de refroidissement',' liquide de refroidissement')])
    date_Rep=models.DateTimeField(null=True)
    desc_Rep=models.CharField(max_length=500)
    Facture=models.IntegerField(null=True)
   
    def __str__(self):
        return self.type_Panne








