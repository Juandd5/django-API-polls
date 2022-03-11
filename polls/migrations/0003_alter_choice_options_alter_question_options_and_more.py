# Generated by Django 4.0.3 on 2022-03-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Respuesta', 'verbose_name_plural': 'Respuestas'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pub_date'], 'verbose_name': 'Pregunta', 'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Published Date'),
        ),
        migrations.AlterModelTable(
            name='choice',
            table='respuestas',
        ),
        migrations.AlterModelTable(
            name='question',
            table='preguntas',
        ),
    ]
