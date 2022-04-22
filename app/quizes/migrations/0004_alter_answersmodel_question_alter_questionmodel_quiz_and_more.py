# Generated by Django 4.0.4 on 2022-04-22 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_remove_quizmodel_only_once_alter_questionmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersmodel',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quizes.questionmodel', verbose_name='Относится к вопросу'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizes.quizmodel', verbose_name='Относится к тесту'),
        ),
        migrations.AlterField(
            model_name='quizurlsmodel',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='quizes.quizmodel', verbose_name='Тест'),
        ),
    ]