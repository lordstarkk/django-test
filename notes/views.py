from django.shortcuts import render, redirect
from .models import Note
from django.views.generic import ListView

def add_note(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Note.objects.create(text=text)
        return redirect('note_list')
    return render(request, 'notes/add_note.html')

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created_at']
