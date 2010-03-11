from django.conf.urls.defaults import *

urlpatterns = patterns('quiz.views',
    url(r'^$', 'quiz_all', name='quiz_all'),
    url(r'^welcome/$', 'quiz_welcome', name='quiz_welcome'),
    url(r'^(?P<quiz_id>\d+)/$', 'quiz_details', name='quiz_details'),

    url(r'^new/$', 'quiz_new', name='quiz_new'),
    url(r'^save/$', 'quiz_save', name='quiz_save'),

    url(r'^edit/(?P<quiz_id>\d+)/$', 'quiz_edit', name='quiz_edit'),
    url(r'^delete/(?P<quiz_id>\d+)/$', 'quiz_delete', name='quiz_delete')
)


