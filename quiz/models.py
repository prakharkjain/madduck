import os
from os import path
from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Quiz(models.Model):
	""" Quiz Model: name, subject, date, class, total_marks, total_questions, duration, note """
	classs = models.CharField(_("class"), max_length=255) 
	subject = models.CharField(_("subject"), max_length=255)
	
	total_marks = models.IntegerField(_("total_marks"))
	total_questions = models.IntegerField(_("total_questions"))
#	duration = models.TimeField()
	
	name = models.CharField(_("name"), max_length=500)
	note = models.CharField(_("note"), max_length=500)
	date = models.DateTimeField(_("added"), default=datetime.now)
	
	class Meta:
		 ordering = ('-date',)

	def get_absolute_url(self):
		return ("describe_quiz", [self.pk])
	get_absolute_url = models.permalink(get_absolute_url)
