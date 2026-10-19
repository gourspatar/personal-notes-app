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
