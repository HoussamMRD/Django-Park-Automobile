from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about us'),
    path('contact/', views.contact, name='contact us'),
    path('login.html/', views.loginEMP, name='login'),
    path('sign.html/', views.sign, name='sign'),




    
    path('dashEMP.html/', views.dashEMP, name='dashEMP'),

    
    path('dashEMP.html/apply-vehicule.html/', views.vehicules, name='applyvehicule'),
    path('dashEMP.html/apply-vehicule.html/history.html/', views.history, name='history'),
    path('dashEMP.html/dashboard.html/apply-vehicule.html/history.html/ServiceRepar.html/', views.Repar, name='Repar'),
    path('dashEMP.html/apply-vehicule.html/history.html/history.html/', views.history, name='history'),
    path('dashEMP.html/dashboard.html/', views.Miss, name='Miss'),
    path('dashEMP.html/dashboard.html/apply-vehicule.html/', views.vehicules, name='applyvehicule'),
    path('dashEMP.html/dashboard.html/apply-vehicule.html/history.html/', views.history, name='history'),
    path('dashEMP.html/dashboard.html/apply-vehicule.html/history.html/ServiceRepar.html/ask-question.html/', views.askQuestion, name='askQuestion'),
    path('dashEMP.html/dashboard.html/apply-vehicule.html/history.html/ServiceRepar.html/ask-question.html/question-history.html/', views.questions, name='questions'),

   
   






]