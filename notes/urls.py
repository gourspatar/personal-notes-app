from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/<int:pk>/", views.note_detail, name="detail"),
]
