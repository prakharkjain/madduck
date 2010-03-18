#from django
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from quiz.models import Quiz
from quiz.forms import QuizForm

# Create your views here.

@login_required
def quiz_all(request):
  """ returns a list of all the quiz created by a user."""
  elements, activity, events = range(10), range(5), range(5)
  
  return render_to_response('quiz/list_all.html', {
        "list" : elements,
        "events" : events,
        "activity" : activity,
  	}, context_instance=RequestContext(request))


#marked for removal.
@login_required
def quiz_first_time(request):
  """ returns a quiz page, when visited for the first time by a user."""
  elements, activity, events = range(10), range(5), range(5)
  
  return render_to_response('quiz/list_all.html', {
        "list" : elements,
        "events" : events,
        "activity" : activity,
      }, context_instance=RequestContext(request))
  
@login_required
def quiz_details(request, quiz_id):
  """ returns the details of a given quiz-id."""
  return render_to_response('quiz/details.html')
  
  
@login_required
def quiz_new(request):
   """ returns a template to create a new quiz. """
   if request.method == "POST":
      quiz_form = QuizForm(request.POST, request.FILES)
      if quiz_form.is_valid():
         new_quiz = quiz_form.save(commit=False)
         new_quiz.save()
         return HttpResponseRedirect(reverse("quiz.views.quiz_new1"))
         
   #GET Request
   else:
       	quiz_form = QuizForm()
        return render_to_response('quiz/new.html', {
                "quiz_form" : quiz_form,
                "events" : range(10),
                "questions" : range(20)
        }, context_instance=RequestContext(request))

   return render_to_response('quiz/new.html', {
        "quiz_form" : quiz_form,
        "events" : range(10),
        "questions" : range(20)
      }, context_instance=RequestContext(request))

#marked for removal; this is a temporary function.
@login_required
def quiz_new1(request):
  """ returns a template to create a new quiz. """
  events, questions = range(10), range(20)
  return render_to_response('quiz/new1.html', {
        "events" : events,
        "questions" : questions
      }, context_instance=RequestContext(request))
  
@login_required
def quiz_save(request):
  """ returns a template to create a new quiz. """
  return render_to_response('quiz/save.html')
  
  
@login_required
def quiz_edit(request, quiz_id):
  """ returns the given quiz preloaded, ready for edit. """
  return render_to_response('quiz/edit.html')
  
@login_required
def quiz_delete(request, quiz_id):
  """ handles the delete for a given quiz. """
  return render_to_response('quiz/delete.html')

@login_required
def welcome(request):
  """ returns a quiz page, when visited for the first time by a user."""
  elements, activity, events = range(10), range(5), range(5)
  
  return render_to_response('quiz/welcome.html', {
        "list" : elements,
        "events" : events,
        "activity" : activity,
      }, context_instance=RequestContext(request))
  
@login_required
def quiz_welcome(request):
  """ returns a quiz page, when visited for the first time by a user."""
  elements, activity, events = range(10), range(5), range(5)
  
  return render_to_response('quiz/welcome-quiz.html', {
        "list" : elements,
        "events" : events,
        "activity" : activity,
      }, context_instance=RequestContext(request))
  
