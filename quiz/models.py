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
    
    """ @TODO these should not be hardcoded.. """
    CLASS_CHOICES = (
        (u"7", "7th Standard"),
        (u"8", "8th Standard"),
        (u"9", "9th Standard"),
        (u"10", "10th Standard"),
    )
    
    """ @TODO these should not be hardcoded.. """
    SUBJECT_CHOICES = (
        (u"ENGLISH", u"English"),
        (u"HISTORY", u"History"),
        (u"GEOGRAPHY", u"Geography"),
        (u"MATHS", u"Mathematics")
    )
    
    """ @TODO these should not be hardcoded.. """
    DURATION_CHOICES = (
        (30, u"30 minutes"),
        (45, u"45 minutes"),
        (60, u"60 minutes"),
        (90, u"1 hour, 30 minutes.")
    )
    
    classs = models.CharField(_("Class"), max_length=15, choices=CLASS_CHOICES, default=_("select a class")) 
    subject = models.CharField(_("Subject"), max_length=15, choices=SUBJECT_CHOICES, default=_("select a subject"))
    
    total_marks = models.IntegerField(_("Total Marks"))
    total_questions = models.IntegerField(_("Total Questions"))
    duration = models.IntegerField(_("Duration Of The Test"), choices=DURATION_CHOICES, default=_("select test duration"))
    
    name = models.CharField(_("Quiz Name"), max_length=500)
    note = models.TextField(_("Quiz Note"), default="any additional notes, hints along with the test...")
    
    """ @TODO rename it to added. """
    added = models.DateTimeField(_("Date (Duration of Test)"), default=datetime.now)
    
    """ @TODO add a new field, last-updated. """
    last_updated = models.DateField(_("Last Updated"), default=datetime.now)

    
    class Meta:
        ordering = ('-last_updated', '-added',)
    
    @models.permalink
    def get_absolute_url(self):
        return ("quiz_view", [self.pk])
    
    def __unicode__(self):
        return "#%d, %s" % (self.id, self.name)
    
class Question(models.Model):
    qQuiz = models.ForeignKey(Quiz)
    qText = models.TextField(_("Question Text"), default="type in the question here.")
    qAnswer = models.TextField(_("Question Answer"), default="type in the answer here.")
    
    class Meta:
        ordering = ("-qText",)
    
    @models.permalink
    def get_absolute_url(self):
        return ("describe_question", [self.pk])
    
    def __unicode__(self):
        return "#%d, %s" % (self.id, self.qText)
    
    