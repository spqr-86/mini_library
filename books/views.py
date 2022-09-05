from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .mixins import JsonableResponseMixin
from .models import Book
from .forms import BookForm


class IndexView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/index.html'


class BookDetailView(DetailView):
    model = Book


class BookNew(JsonableResponseMixin, LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = 'books/formBook.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookUpdate(JsonableResponseMixin, LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/formBook.html'
    success_url = reverse_lazy('index')


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_check_delete.html'
    success_url = reverse_lazy('index')
