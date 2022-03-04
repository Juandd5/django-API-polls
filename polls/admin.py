from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)#Esta función lleva como parámetro el modelo que queremos poner disponible en el adminitrador
admin.site.register(Choice)
