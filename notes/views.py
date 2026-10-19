from django.shortcuts import render
from .models import Note

# Create your views here.


def home(request):
    notes = Note.objects.all().order_by("-created_at")

    context = {
        "notes": notes,
    }

    return render(request, "notes/home.html", context)
