# Python
from datetime import timedelta

#Django
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published Date', auto_now_add=True)

    def __str__(self) -> str:
        return self.question_text

    def was_created_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - timedelta(days=1)

    class Meta():
        ordering = ['pub_date']
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        db_table = 'preguntas' #Nombre de la tabla en la base de datos

    def clean(self):
        if self.choice_set.count() < 1:
            raise ValidationError('Question must have at least one choice')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
    
    class Meta():
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        db_table = 'respuestas'
