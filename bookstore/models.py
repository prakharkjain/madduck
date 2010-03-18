import os
from os import path
from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Book(models.Model):
	"""
	Book Model : title, publisher, author, description, coverart, adder, added 
	""" 
	title = models.CharField(_('title'), max_length=255)
	author = models.CharField(_('author'), max_length=255)
	publisher = models.CharField(_('publisher'), max_length=255)
	description = models.TextField(_('description'), blank=True)
	coverart = models.ImageField(upload_to="bookstore", blank=True, null=True)
	
	adder = models.ForeignKey(User, related_name="added_books", verbose_name=_('adder'))
	added = models.DateTimeField(_('added'), default=datetime.now)
	
	def get_absolute_url(self):
		return ("describe_book", [self.pk])
	get_absolute_url = models.permalink(get_absolute_url)
	
	class Meta:
		ordering = ('-added', )
	
	def _get_thumb_url(self, folder, size):
		""" get a thumbnail, given a folder and a size """
		if not self.coverart:
			return '#'

		upload_to = path.dirname (self.coverart.path)
		tiny = path.join(upload_to, folder, path.basename(self.coverart.path))
		tiny = path.normalpath(tiny)
		if not path.exists(tiny):
			import Image
			im = Image.open(self.coverart.path)
			im = Image.thumbnail(size, Image.ANTIALIAS)
			im.save(tiny, 'JPEG')
		
		return path.join(path.dirname(self.coverart.url), folder, path.basename(self.coverart.path)).replace('\\', '/')
	
	def get_thumb_url(self):
		return self._get_thumb_url('thumb_100_100', (100,100))
	
	def thumb(self):
		""" get thumb <a>. """

		link = self.get_thumb_url()
		if link is None:
			return '<a href="#" target="_blank"  >NO IMAGE</a>'
		else:
			return '<img src="%s" />' % (link)
	thumb.allow_tags = True

	def fullpicture(self):
		""" get full picture <a> """
		link = "%s%s" % (settings.MEDIA_URL, self.coverart)
		if link is None:
			return '<a href="#" target="_blank"  >NO IMAGE</a>'
		else:
			return '<img src="%s" />' % (link)
	fullpicture.allow_tags = True
