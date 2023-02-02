from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Author, Books
from .forms  import BookForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

class Home(TemplateView):
    template_name = 'home.html'

class BookList(ListView):
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'books'

class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class CreateBook(CreateView):
    model = Books
    fields = '__all__' 
    template_name = 'create_book.html'
    success_url = '/books/'

class ViewBook(DetailView):
    model = Books
    template_name = 'detail_book.html'
    context_object_name = 'book'

class UpdateBook(UpdateView):
    model = Books
    template_name = 'update_book.html'
    fields = '__all__'
    success_url = '/books/'


class DeleteBook(DeleteView):
    model = Books
    template_name = 'delete_book.html'
    success_url = reverse_lazy('books')

    def post(self, request, *args, **kwargs):
        if request.POST["cancel"]:
            return redirect('/books/')
        else:
            return super(DeleteBook, self).post(request, *args, **kwargs)