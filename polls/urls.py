from django.urls import path

from . import views #del paquete polls import ...

urlpatterns = [
    #ex: /polls
    path('', views.index, name='index'), #index es la función que creé en views, le agrego un nombre descriptivo
    #ex: /polls/5
    path('<question_id>', views.detail, name='detail'),
    #ex: /polls/results
    path('<question_id>/results', views.results, name='results'),
    #ex: /polls/vote
    path('<question_id>/vote', views.vote, name='vote')
]