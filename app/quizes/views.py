from django.shortcuts import render, get_object_or_404
from quizes import models
import logging


def quiz_template(request):
    return render(request, 'quizes/full/quiz.html')


def home_template(request):
    return render(request, 'quizes/full/home.html')


def result_template(request):
    return render(request, 'quizes/full/result.html')


def quiz(request, uuid):
    quiz_object = models.QuizModel.objects.get(uuid=uuid)
    context = {
        'quiz': quiz_object,
    }
    return render(request, 'quizes/quiz.html', context)


def home(request):
    context = {'quizes': list(models.QuizModel.objects.all())}
    logger = logging.getLogger(__name__)
    logger.info("LOG")
    return render(request, 'quizes/home.html', context)


def accept_quiz(request):
    student = request.POST.get('student-name')
    group = request.POST.get('student-group')
    email = request.POST.get('student-email')
    quiz_id = request.POST.get('quiz-id')

    quiz = get_object_or_404(models.QuizModel, id=quiz_id)
    question_amount = len(quiz.questions.all())
    right_answers_amount = 0

    debug = []

    for field in request.POST:
        if field.startswith('answer'):

            question_id = int(field.split('-')[-1])
            question = quiz.questions.get(id=question_id)

            debug.append([question, question.right_answer, question.right_answer.id])
            if question.right_answer.id == int(request.POST.get(field)):
                right_answers_amount += 1

        elif field.startswith('text-answer'):
            question_id = int(field.split('-')[-1])

            question = quiz.questions.get(id=question_id)
            answer = request.POST.get(field).strip().lower()
            right_answer = question.right_answer.text.strip().lower()

            if answer == right_answer:
                right_answers_amount += 1

    result = models.CompletedQuizModel.objects.create(
        student=student,
        group=group,
        email=email,
        quiz=quiz,
        result=f'{right_answers_amount} из {question_amount}'
    )

    return render(request, 'quizes/result.html', {'result': result, 'post': request.POST, 'debug': debug})
