from django.conf.urls.defaults import patterns, url
from django.views.generic import list_detail
from books.models import Book

books_info = {
   'queryset': Book.objects.all(),
   'template_name': 'books/list.html',
   'template_object_name': 'book',  # object_list --> book_list
   'extra_context': {},
}

urlpatterns = patterns('',
    url(r'^preporuke/$', list_detail.object_list, books_info, name='book_list'),
)
