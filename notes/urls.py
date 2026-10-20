from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/<int:pk>/", views.note_detail, name="detail"),
    path("notes/<int:pk>/edit/", views.note_edit, name="edit"),
    path("notes/<int:pk>/delete/", views.note_delete, name="delete"),
]
