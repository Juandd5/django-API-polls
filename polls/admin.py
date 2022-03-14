from django.contrib import admin
from .models import Question, Choice


#Con esto, cuando cree preguntas, puedo agregar hasta 3 respuestas.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] #Organizo el orden en que se muestran estos campos
    inlines = [ChoiceInLine] #Relaciono el ChoiceInLine
    list_display = ('question_text', 'pub_date', 'was_created_recently') #Añado más campos para visualizar
    list_filter = ['pub_date'] #añade un recuadro para filtrar por fechas
    search_fields = ['question_text'] #añade un cuadro para buscar preguntas


admin.site.register(Question, QuestionAdmin)#Esta función lleva como parámetro el modelo que queremos poner disponible en el adminitrador
#admin.site.register(Choice)
