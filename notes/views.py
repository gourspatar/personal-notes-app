from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def home(request):
    search_query = request.GET.get("q", "")

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

    if search_query:
        notes = notes.filter(title__icontains=search_query)

    context = {
        "notes": notes,
        "form": form,
        "search_query": search_query,
    }

    return render(request, "notes/home.html", context)


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    context = {
        "note": note,
    }

    return render(request, "notes/note_detail.html", context)


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

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


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("notes:home")

    context = {
        "note": note,
    }

    return render(request, "notes/note_confirm_delete.html", context)
