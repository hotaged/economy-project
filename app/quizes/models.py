from django.db import models
from uuid import uuid4


class QuizModel(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название теста', unique=True)
    uuid = models.UUIDField(default=uuid4, unique=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title

    def shuffled_questions(self):
        import random

        questions = list(self.questions.all())
        random.shuffle(questions)
        return questions


class QuestionModel(models.Model):
    TYPES = (
        ('MW', 'Missing Word'),
        ('AN', 'Anagram'),
        ('GZ', 'GameShow Quiz')
    )

    question = models.TextField(verbose_name='Вопрос')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Изображение')
    type = models.CharField(max_length=2, choices=TYPES, default=TYPES[2][0], verbose_name='Тип')
    right_answer = models.ForeignKey('AnswersModel', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Верный ответ')
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, verbose_name='Относится к тесту', related_name='questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question.__str__()[0:50]

    def shuffled_answers(self):
        import random
        answers = list(self.answers.all())
        random.shuffle(answers)
        return answers

    def anagram_answer(self):
        import random
        answer = self.right_answer.text.__str__()

        length = len(answer)
        sign = random.choice(answer)
        resp = []

        for i in range(length):
            if answer[i] == sign:
                resp.append(sign)
            else:
                resp.append('_')

        return ' '.join(resp)


class AnswersModel(models.Model):
    text = models.CharField(max_length=512, verbose_name='Текст ответа')
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, verbose_name='Относится к вопросу', related_name='answers')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.text


class QuizUrlsModel(models.Model):
    quiz_url = models.URLField(verbose_name='Ссылка на прохождение теста')
    quiz = models.ForeignKey(QuizModel, verbose_name='Тест', on_delete=models.CASCADE, related_name='urls')

    class Meta:
        verbose_name = 'Ссылка на тест'
        verbose_name_plural = 'Ссылки на тесты'


class CompletedQuizModel(models.Model):
    student = models.CharField(verbose_name='Ф.И.О Студента: ', max_length=64)
    email = models.EmailField(verbose_name='Email: ', max_length=64)
    group = models.CharField(verbose_name='Группа: ', max_length=8)
    result = models.CharField(verbose_name='Результат: ', max_length=32)

    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, verbose_name='Пройденый тест:')

    class Meta:
        verbose_name = 'Отчет по тесту'
        verbose_name_plural = 'Отчеты по тестам'


