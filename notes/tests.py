from django.test import TestCase
from django.urls import reverse

from .models import Note

# Create your tests here.


class NoteTests(TestCase):
    def test_homepage_loads(self):
        response = self.client.get(reverse("notes:home"))

        self.assertEqual(response.status_code, 200)

    def test_create_note(self):
        response = self.client.post(
            reverse("notes:home"),
            {
                "title": "Test Note",
                "content": "This is a test note.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Test Note").exists())

    def test_note_detail_page(self):
        note = Note.objects.create(
            title="Detail Test",
            content="Testing the detail page.",
        )

        response = self.client.get(reverse("notes:detail", args=[note.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Detail Test")
        self.assertContains(response, "Testing the detail page.")

    def test_edit_note(self):
        note = Note.objects.create(
            title="Old Title",
            content="Old content",
        )

        response = self.client.post(
            reverse("notes:edit", args=[note.pk]),
            {
                "title": "Updated Title",
                "content": "Updated content",
            },
        )

        self.assertEqual(response.status_code, 302)

        note.refresh_from_db()
        self.assertEqual(note.title, "Updated Title")
        self.assertEqual(note.content, "Updated content")
        self.assertEqual(Note.objects.count(), 1)

    def test_delete_note(self):
        note = Note.objects.create(
            title="Delete Me",
            content="Content to delete",
        )

        response = self.client.post(reverse("notes:delete", args=[note.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=note.pk).exists())

    def test_search_notes_by_title(self):
        Note.objects.create(
            title="Learn Django",
            content="Django notes",
        )
        Note.objects.create(
            title="Learn Python",
            content="Python notes",
        )

        response = self.client.get(
            reverse("notes:home"),
            {"q": "django"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django")
        self.assertNotContains(response, "Learn Python")

    def test_note_timestamps(self):
        note = Note.objects.create(
            title="Timestamp Test",
            content="Testing timestamps",
        )

        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

        original_created_at = note.created_at

        note.title = "Updated Timestamp Test"
        note.save()
        note.refresh_from_db()

        self.assertEqual(note.created_at, original_created_at)
        self.assertGreaterEqual(note.updated_at, original_created_at)

    def test_edit_nonexistent_note_returns_404(self):
        response = self.client.get(reverse("notes:edit", args=[99999]))

        self.assertEqual(response.status_code, 404)

    def test_delete_requires_post_to_delete(self):
        note = Note.objects.create(
            title="Keep Me",
            content="This note should remain",
        )

        response = self.client.get(reverse("notes:delete", args=[note.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(pk=note.pk).exists())
