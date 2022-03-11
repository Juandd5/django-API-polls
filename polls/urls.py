from django.urls import path

from . import views #del paquete polls import ...

app_name = 'polls'
urlpatterns = [
    #ex: /polls
    path('', views.IndexView.as_view(), name='index'), #index es la función que creé en views, le agrego un nombre descriptivo
    #ex: /polls/5
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    #ex: /polls/results
    path('<int:pk>/results', views.ResultView.as_view(), name='results'),
    #ex: /polls/vote
    path('<int:question_id>/vote', views.vote, name='vote')
]