from django.shortcuts import redirect, render
from . forms import *
from django.contrib import messages
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Note Added from {request.user.username} Successfully")
    else:
        form = NotesForm()

    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes, 'form':form}
    return render(request, 'dashboard/notes.html', context)

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailView(DetailView):
    model = Notes

def homework(request):
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    
    context = {'homeworks': homework, 'homework_done': homework_done}
    return render(request, 'dashboard/homework.html', context)
    
    
