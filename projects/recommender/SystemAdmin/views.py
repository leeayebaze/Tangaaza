from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import loader
from django.urls import reverse

# Create your views here.
from Scripts.SimpleRecommender import RecommenderClass 
from Scripts.SimpleRecommender2 import Recommender2Class
from Scripts.SVD import svdclass

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else: 
        data=RecommenderClass.recommenderFn(request)   
        data2=Recommender2Class.recommender2Fn(request)       
        finalpredic=svdclass.svdfn(request)
        print(data, data2, finalpredic)
        template = loader.get_template('SystemAdmin/index.html')
        context = {    
            'movies': data,
            'recommendationsystem': data2,
            'Finalpredictions':finalpredic
            
        }
        return HttpResponse(template.render(context, request))

def logout(request):
    return render(request, 'recommender/templates/registration/login.html')      

