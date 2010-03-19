from django.conf.urls.defaults import *

urlpatterns = patterns('quiz.views',
    url(r'^$', 'quiz_all', name='quiz_all'),
    url(r'^welcome/$', 'welcome', name='welcome'),

    url(r'^create/$', 'quiz_create', name='quiz_create'),
    url(r'^view/(?P<quiz_id>\d+)/$', 'quiz_view', name='quiz_view'),
    url(r'^update/(?P<quiz_id>\d+)/$', 'quiz_update', name='quiz_update'),
    url(r'^delete/(?P<quiz_id>\d+)/$', 'quiz_delete', name='quiz_delete'),
    
    url(r'^question-new/$', 'question_new', name='question_new'),
    
    #marked for removal.
    url(r'^save/$', 'quiz_save', name='quiz_save'),
)
