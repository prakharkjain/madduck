from django.conf.urls.defaults import *
from bookstore.models import Book

urlpatterns = patterns('bookstore.views',
		url(r'^$', 'books', name='all_books'),
		url(r'^(?P<book_id>\d+)/book/$', 'book', name='describe_book'),
		url(r'^your_books/$', 'your_books', name='your_books'),
		url(r'^user_books/(?P<username>\w+)/$', 'user_books', name='describe_book'),
		#CRUD URLs
		url(r'^add/', 'add_book', name='add_book'),
		url(r'^(?P<book_id>\d+)/update/$', 'update_book', name='update_book'),
		url(r'^(?P<book_id>\d+)/delete/$', 'delete_book', name='delete_book'),
)
