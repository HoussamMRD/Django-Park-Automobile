from django.contrib import admin
from .models import vehicule
from .models import employe
from .models import mission
from .models import Question
from .models import Location
from .models import Reparation




class vehiculeAdmin(admin.ModelAdmin):
    list_display = ( 'marque', 'matricule',  'modele', 'couleur', 'Availability', 'typeCarburant')    
    list_filter = ('Availability', ) 
    search_fields = ( 'Availability', )



class employeAdmin(admin.ModelAdmin):
    list_display = ( 'nom', 'prenom', 'adresse' ,'category_Permis' ,  'telephone', 'disponibilite' , )
    list_filter = ('category_Permis' , 'disponibilite', )
    search_fields = (  'category_Permis' , 'disponibilite',)


class missionAdmin(admin.ModelAdmin):
    list_display = ( 'typeM' ,  'vehicule', 'employe')
    list_filter = ('typeM', )
    search_fields = ( 'typeM',)


class locationAdmin(admin.ModelAdmin):
    list_display = ( 'vehicule' ,  'type_Location', 'Start_Location', 'End_Location',)
    list_filter = ('type_Location', )
    search_fields = ( 'type_Location',)

class reparationsAdmin(admin.ModelAdmin):
    list_display = ( 'vehicule' ,  'type_Panne', 'date_Rep', 'Facture' )
    list_filter = ('type_Panne', )
    search_fields = ( 'type_Panne',)




# Register your models here.
admin.site.register(vehicule, vehiculeAdmin)
admin.site.register(employe, employeAdmin)
admin.site.register(mission, missionAdmin)
admin.site.register(Question)
admin.site.register(Location, locationAdmin)
admin.site.register(Reparation, reparationsAdmin)
