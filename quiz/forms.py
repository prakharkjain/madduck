#from django
from django import forms
from django.utils.translation import ugettext_lazy as _

#from bookstore
from quiz.models import Quiz, Question

class QuizForm(forms.ModelForm):
    """ 
    Quiz Form : form associated to the quiz model
    """
    def __init__ (self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)

    def clean(self):
        """ do validation here. """
        #name is mandatory
        if 'name' not in self.cleaned_data:
            return
        #if a book with that title already exists
#        if Quiz.objects.filter(name=self.cleaned_data['name']).count() > 0:
#            raise forms.ValidationError(_("This quiz already exists"))
        return self.cleaned_data
        
    class Meta:
        model = Quiz
        exclude = ('date',)
        fields = ('classs', 'subject', 'duration', 'name', 'total_marks', 'total_questions', 'note')

class QuestionForm(forms.ModelForm):
    """ Question Form : form associated to the question model. """
    def __init__ (self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.is_update = False
        
    def clean(self):
        """ do question form validation here. """
        if 'qText' not in self.cleaned_data:
            return
        return self.cleaned_data
        
    class Meta:
        model = Question