from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
            )
            return redirect("notes:home")
    else:
        form = NoteForm()

    notes = Note.objects.all().order_by("-created_at")

    context = {
        "notes": notes,
        "form": form,
    }

    return render(request, "notes/home.html", context)


def note_detail(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        "note": note,
    }

    return render(request, "notes/note_detail.html", context)


def note_edit(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note.title = form.cleaned_data["title"]
            note.content = form.cleaned_data["content"]
            note.save()

            return redirect("notes:detail", pk=note.pk)
    else:
        form = NoteForm(
            initial={
                "title": note.title,
                "content": note.content,
            }
        )

    context = {
        "form": form,
        "note": note,
    }

    return render(request, "notes/note_edit.html", context)
