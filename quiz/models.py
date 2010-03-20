import os
from os import path
from datetime import datetime

from django.db import models
from django.db.models import permalink
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.base import get_absolute_url

# Create your models here.
class Quiz(models.Model):
    """ Quiz Model: name, subject, date, class, total_marks, total_questions, duration, note """
    classs = models.CharField(_("Class"), max_length=255) 
    subject = models.CharField(_("Subject"), max_length=255)
    
    total_marks = models.IntegerField(_("Total Marks"))
    total_questions = models.IntegerField(_("Total Questions"))
#    duration = models.TimeField()
    
    name = models.CharField(_("Quiz Name"), max_length=500)
    note = models.CharField(_("Quiz Note"), max_length=500)
    date = models.DateTimeField(_("Date (Duration of Test)"), default=datetime.now)
    
    class Meta:
        ordering = ('-date',)
    
    @models.permalink
    def get_absolute_url(self):
        return ("quiz_view", [self.pk])

class Question(models.Model):
    qText = models.TextField(_("Question Text"), default="type in the question here.")
    qAnswer = models.TextField(_("Question Answer"), default="type in the answer here.")
    
    class Meta:
        ordering = ("-qText",)
    
    @models.permalink
    def get_absolute_url(self):
        return ("describe_question", [self.pk])
    