from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from platformdirs import user_log_dir
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

from django.contrib.auth.models import User

from park.models import Question, Reparation, employe, mission, vehicule


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about')

def contact(request):
    return render(request, 'pages/contact')


def loginEMP(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashEMP')
    return render(request, 'pages/login.html')
    
def sign(request):
    form=UserForm()

    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
        return redirect('login')

    context={'form':form}
    return render(request, 'pages/sign.html', context)










def dashEMP(request):
    return render(request, 'pages/dashEMP.html')









def vehicules(request):
    
    vehicules=vehicule.objects.filter(Availability='Dispo')
    
    return render(request, 'pages/apply-vehicule.html', {'vehicules': vehicules})


def history(request):
    vehicules=vehicule.objects.filter(Status='Aprov')
    return render(request, 'pages/history.html',{'vehicules': vehicules})




def Miss(request):
    
    Miss=mission.objects.all
    
    return render(request, 'pages/dashboard.html', {'Miss': Miss})



def askQuestion(request):
    return render(request, 'pages/ask-question.html')

def questions(request):
    questions=Question.objects.all()
    return render(request, 'pages/question-history.html',{'questions': questions})








def Repar(request):
    
    Repar=Reparation.objects.all()
    
    return render(request, 'pages/ServiceRepar.html', {'Repar': Repar})

