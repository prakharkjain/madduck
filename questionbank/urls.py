from django.conf.urls.defaults import *
from questionbank.models import Question

urlpatterns = patterns(	'questionbank.views', 
		url(r'^$', 'questionbank_index', name='questionbank-index'),
		url(r'^all/$', 'questionbank_all', name='questionbank-all'),
		url(r'^details/(?P<id>\d+)/$', 'questionbank_details', name='questionbank-details'),
		#CRUD URLs.
		url(r'^add/$', 'questionbank_add', name='questionbank-add'),
		url(r'^edit/(?P<id>\d+)/$', 'questionbank_edit', name='questionbank-edit'),
		url(r'^delete/(?P<id>\d+)/$', 'questionbank_delete', name='questionbank-delete'),
)
