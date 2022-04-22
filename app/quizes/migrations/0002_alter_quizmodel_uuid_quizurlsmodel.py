# Generated by Django 4.0.4 on 2022-04-21 20:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.CreateModel(
            name='QuizUrlsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_url', models.URLField(verbose_name='Ссылка на прохождение теста')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quizmodel', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Ссылка на тест',
                'verbose_name_plural': 'Ссылки на тесты',
            },
        ),
    ]