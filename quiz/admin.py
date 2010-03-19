from django.contrib import admin
from quiz.models import Quiz
from quiz.models import Question

class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'classs', 'total_marks', 'total_questions')
admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qText', 'qAnswer')
admin.site.register(Question, QuestionAdmin)
