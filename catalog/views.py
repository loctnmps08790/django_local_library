from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from . import models
from . import forms


# Create your views here.
def index(request):
    num_visited = request.session.get('visited', 0)
    request.session['visited'] = num_visited + 1
    context = {
        'visited': num_visited
    }
    return render(request, 'catalog/index.html', context=context)


@login_required
def contact_view(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
    else:
        form = forms.ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'catalog/contact.html', context=context)


def book_form_view(request):
    form = forms.BookForm()
    context = {
        'form': form,
    }
    return render(request, 'catalog/bookform.html', context=context)


class BookCreate(generic.CreateView):
    model = models.Book
    fields = '__all__'


class BookListView(LoginRequiredMixin, generic.ListView):
    model = models.Book
    paginate_by = 10


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = models.Author


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Book


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Author
