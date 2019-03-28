from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import loader
from django.urls import reverse

from django.shortcuts import get_object_or_404, render

#from .models import Choice, Question
from Scripts.SimpleRecommender import RecommenderClass 
from Scripts.SimpleRecommender2 import Recommender2Class
from Scripts.totalratings import totalratingclass
from Scripts.genreapperanace import genreappearanceclass
from Scripts.color import colorclass
from Scripts.SVDPLUS import SVDD

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    data=RecommenderClass.recommenderFn(request)
    print(data)
    template = loader.get_template('movies/index.html')
    context = {
        'movies': data
    }
    return HttpResponse(template.render(context, request))

def market(request):
    totalrate=totalratingclass.totalratingfn(request)
    sumgenre=genreappearanceclass.genreappearancefn(request)
    colorclass.colorfn(request)
    print(totalrate, sumgenre)
    template = loader.get_template('movies/marketing.html')
    context = {
        'rate': totalrate,
        'Totalgenre':sumgenre
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)






