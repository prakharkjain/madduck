from django.conf.urls.defaults import *

urlpatterns = patterns('quiz.views',
    url(r'^$', 'quiz_view_all', name='quiz_view_all'),
    url(r'^welcome/$', 'quiz_welcome', name='quiz_welcome'),
    
    url(r'^create/$', 'quiz_create', name='quiz_create'),
    url(r'^view/(?P<quiz_id>\d+)/$', 'quiz_view', name='quiz_view'),
    url(r'^update/(?P<quiz_id>\d+)/$', 'quiz_update', name='quiz_update'),
    url(r'^delete/(?P<quiz_id>\d+)/$', 'quiz_delete', name='quiz_delete'),
    
    url(r'^(?P<quiz_id>\d+)/question-new/$', 'question_new', name='question_new'),
    url(r'^(?P<quiz_id>\d+)/question-view/(?P<question_id>\d+)$', 'question_view', name='question_view'),
    
)
