from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Question(models.Model):
	"""
	Question Model : title, author, description, published, adder, added
	"""
	QUESTION_TYPES = (
		(u'ES', u'Essay Type'),
		(u'TF', u'True or False'),
		(u'MS', u'Multiple Choice (single correct)'),
		(u'MM', u'Multiple Choice (multiple correct)'),
		(u'MA', u'Match The Folowing'),
	)

	title = models.CharField(_("title"), max_length=500)
	type = models.CharField(_("question type"), max_length=2, choices=QUESTION_TYPES)
	description = models.TextField(_("question description"), blank=False)
	published = models.BooleanField(_("is published"), default=False)

	adder = models.ForeignKey(User, related_name="added_questions", verbose_name=_("question added by"))
	added = models.DateTimeField(_("added on"), default=datetime.now)

	class Meta:
		ordering = ('-added', )
	
	def __unicode__(self):
		return self.title
 
#	@models.permalink
#	def get_absolute_url(self):
#		return ("questionsbank-details", [str(self.pk)])


class Answers(models.Model):
	
	question = models.ForeignKey(Question)
	answer = models.CharField(_("answer"), max_length=200)
	marks = models.IntegerField(_("marks"))
	correct = models.BooleanField(_("is correct"))
	
	def __unicode__(self):
		return self.answer
