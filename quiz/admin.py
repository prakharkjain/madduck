from django.contrib import admin
from quiz.models import Quiz, Question

class QuizAdmin(admin.ModelAdmin):
    list_display = ('classs', 'subject', 'total_marks', 'total_questions')
admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qText', 'qAnswer')
admin.site.register(Question, QuestionAdmin)
