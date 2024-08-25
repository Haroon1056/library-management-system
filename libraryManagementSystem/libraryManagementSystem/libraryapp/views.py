from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def home(request):
    return render(request, 'home.html')

def load_form(request):
    form = BookForm
    return render(request, 'load_form.html', {'form': form})

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        form.save()
        return redirect('/show')
    else:
        form = BookForm()
def show(request):
    book = Book.objects.all
    return render(request, 'show.html', {'book': book})

def edit(request, id):
    book = Book.objects.get(id=id)
    return render(request, "edit.html", {'book': book})

def update(request, id):
    book =Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    form.save()
    return redirect('/show')

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/show')
    
def search(request):
    given_name = request.POST['name']
    book = Book.objects.filter(title__icontains=given_name)
    return render(request, "show.html", {'book':book})
# Create your views here.
