#from django
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from quiz.models import Quiz, Question
from quiz.forms import QuizForm, QuestionForm

@login_required
def quiz_welcome(request):
  """ returns a quiz page, when visited for the first time by a user."""
  elements, activity, events = range(10), range(5), range(5)
  
  return render_to_response('quiz/welcome.html', {
               "list" : elements,
               "events" : events,
               "activity" : activity,
         }, context_instance=RequestContext(request))

@login_required
def quiz_view_all(request):
  """ returns a list of all the quiz created by a user."""
  elements, activity, events = range(10), range(5), range(5)
  quiz_list = Quiz.objects.all().order_by('-added')

  return render_to_response('quiz/view_quiz_all.html', {
                "quiz_list" : quiz_list,
                "events" : events,
                "activity" : activity,
          }, context_instance=RequestContext(request))

@login_required
def quiz_view(request, quiz_id):
  """ returns the details of a given quiz-id."""
  quiz = get_object_or_404(Quiz, id=quiz_id)
  return render_to_response('quiz/view_quiz.html', {
            "quizobj" : quiz,
          }, context_instance=RequestContext(request))

@login_required
def quiz_create(request):
   """ returns a template to create a new quiz. """
   if request.method == "POST":
      quiz_form = QuizForm(request.POST, request.FILES)
      if quiz_form.is_valid():
         new_quiz = quiz_form.save(commit=False)
         new_quiz.save()
         return HttpResponseRedirect(reverse("quiz.views.question_new", args=[new_quiz.id]))
         
   #GET Request
   else:
        quiz_form = QuizForm()
        return render_to_response('quiz/create_quiz.html', {
                    "quiz_form" : quiz_form,
                    "events" : range(10),
                    "questions" : range(20)
                }, context_instance=RequestContext(request))

   return render_to_response('quiz/create_quiz.html', {
                "quiz_form" : quiz_form,
                "events" : range(10),
                "questions" : range(20)
           }, context_instance=RequestContext(request))

#marked for removal; this is a temporary function.

@login_required
def quiz_update(request, quiz_id):
    """ update the quiz, given its id. """
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == "POST":
        quiz_form = QuizForm(request.POST, request.FILES, instance=quiz)
        quiz_form.is_update = True
        if quiz_form.is_valid():
            quiz_form.save()
            return HttpResponseRedirect(reverse("quiz.views.quiz_update", args=[quiz_id]))
    else:
        quiz_form = QuizForm(instance=quiz)
        return render_to_response("quiz/update_quiz.html", {
                    "quiz_form": quiz_form,
                    "quiz": quiz,
                }, context_instance=RequestContext(request))
    #generic case
    return render_to_response("quiz/update_quiz.html", {
                "quiz_form": quiz_form,
            }, context_instance=RequestContext(request))

@login_required
def quiz_delete(request, quiz_id):
    """ handles the delete for a given quiz. """
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    request.user.message_set.create(message=_("Quiz Deleted."))
    
    return HttpResponseRedirect(reverse("quiz.views.quiz_view_all"))

""" all helper methods related to question creation start from here."""
@login_required
def question_new(request, quiz_id):
   """ returns a template to create a new quiz. """
   if request.method == "POST":
      question_form = QuestionForm(request.POST, request.FILES)
      if question_form.is_valid():
         new_question = question_form.save(commit=False)
         new_question.qQuiz = Quiz.objects.get(id=quiz_id)
         new_question.save()
         return HttpResponseRedirect(reverse("quiz.views.question_new", args=[quiz_id]))
         
   #GET Request
   else:
        question_form = QuestionForm()
        return render_to_response('quiz/create_question.html', {
                    "question_form" : question_form,
                    "events" : range(10),
                    "questions" : range(20)
               }, context_instance=RequestContext(request))

   return render_to_response('quiz/create_question.html', {
                "question_form" : question_form,
                "events" : range(10),
                "questions" : range(20)
          }, context_instance=RequestContext(request))
