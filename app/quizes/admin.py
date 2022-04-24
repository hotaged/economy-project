from django.contrib import admin
from django.contrib.auth.models import Group
from quizes import models


class QuizModelAdmin(admin.ModelAdmin):
    fields = ('title', 'uuid')

    def get_readonly_fields(self, request, obj=None):
        return 'uuid',


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('get_question', )
    list_filter = ('quiz__title', 'type')

    def get_question(self, obj):
        return obj.question.__str__()[0:50]


class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'get_question', 'id')
    list_filter = ('question__quiz__title', 'question__type', 'question__question')
    
    def get_question(self, obj):
        return obj.question.question.__str__()[0:50]


class QuizUrlModelAdmin(admin.ModelAdmin):
    fields = ('quiz_url', )


class CompletedQuizModelAdmin(admin.ModelAdmin):
    fields = ('student', 'group', 'email', 'result', 'quiz')
    list_display = ('student', 'group', 'result', 'quiz')
    list_filter = ('student', 'group', 'result', 'quiz__title')


admin.site.register(models.QuizModel, QuizModelAdmin)
admin.site.register(models.QuestionModel, QuestionModelAdmin)
admin.site.register(models.AnswersModel, AnswerModelAdmin)
admin.site.register(models.QuizUrlsModel, QuizModelAdmin)
admin.site.register(models.CompletedQuizModel, CompletedQuizModelAdmin)

admin.site.unregister(Group)

