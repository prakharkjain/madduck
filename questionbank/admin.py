from django.contrib import admin
from questionbank.models import Question, Answers


class AnswersInline(admin.TabularInline):
	model = Answers
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('title', 'type', 'published', 'adder', 'added')
	list_filter = ['added']
	search_fields = ['title', 'type', 'adder', 'added']
	date_heirarchy = 'added'
	
	fieldsets = [
		('Question Title & Type', {'fields' : ['title', 'type']}),
		('Question Description & Publish Status', {'fields' : ['description', 'published']}),
		('Date Information & User Information', {'fields' : ['adder', 'added'], 'classes' : ['collapse']}),
	]
	inlines = [AnswersInline]

admin.site.register(Question, QuestionAdmin)

