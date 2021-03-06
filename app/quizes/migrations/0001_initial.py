# Generated by Django 4.0.4 on 2022-04-20 16:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512, verbose_name='Текст ответа')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название теста')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('only_once', models.BooleanField(default=False, verbose_name='Может быть пройден один раз')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение')),
                ('type', models.CharField(choices=[('MW', 'Missing Word'), ('MU', 'Match Up'), ('GZ', 'GameShow Quiz')], default='GZ', max_length=2, verbose_name='Тип')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quizmodel', verbose_name='Относится к тесту')),
                ('right_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizes.answersmodel', verbose_name='Верный ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='answersmodel',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.questionmodel', verbose_name='Относится к вопросу'),
        ),
    ]
