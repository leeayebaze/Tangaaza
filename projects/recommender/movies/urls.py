from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
#    path('', views.current_datetime, name='index'),
    path('market', views.market, name='market'),

    path('create', views.index, name='create'),
    #path('create', views.index.create), "This is also correct"

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]