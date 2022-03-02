from django.urls import path
from . import views #del paquete polls import ...

urlpatterns = [
    path('', views.index, name='index') #index es la función que creé en views, le agrego un nombre descriptivo
]