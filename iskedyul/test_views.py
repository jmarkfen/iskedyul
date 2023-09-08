from django.test import TestCase
from django.urls import reverse
from iskedyul.models import Timetable

from iskedyul import views

# Create your tests here.


class TestViews(TestCase):
    """
    test views
    """

    def test_create_timetable(self):
        """
        test the create_timetable page
        """
        response = self.client.get(reverse(views.create_timetable))
        self.assertEqual(response.status_code, 200)
        context = {
            "form_action": reverse(views.save_timetable),
            "next_url": reverse(views.timetable_list),
        }
        # verify the context data exists in the render
        for key, value in context.items():
            self.assertIn(key, response.context)
            self.assertEqual(response.context[key], value)

    def test_save_timetable(self):
        """
        test the save_timetable form action
        """
        # simulate sending post data to /timetable/save
        form_data = {
            "title": "Timetable A",
            "next_url": reverse(views.create_timetable),
        }
        response = self.client.post(reverse(views.save_timetable), data=form_data)
        self.assertEqual(response.status_code, 302)  # redirect status: 302 Found
        # verify the data is saved to database
        saved = Timetable.objects.latest("title")
        self.assertEqual(saved.title, form_data["title"])

    def test_timetable_list(self):
        """
        test the timetable list page
        """
        response = self.client.get(reverse(views.timetable_list))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_timetable_dialog(self):
        """
        test confirmation dialog for deleting timetable
        """
        timetable = Timetable.objects.create(title="Test timetable")
        args = [
            timetable.pk,
        ]
        response = self.client.get(reverse(views.delete_timetable_dialog, args=args))
        self.assertEqual(response.status_code, 200)

    def test_delete_timetable(self):
        """
        test deleting timetable
        """
        timetable = Timetable.objects.create(title="Test timetable")
        form_data = {
            "id": timetable.pk,
            "button_choice": "ok",
            "next_url": reverse(views.timetable_list),
        }
        response = self.client.post(reverse(views.delete_timetable), data=form_data)
        self.assertEqual(response.status_code, 302)  # redirect status: 302 Found
        # verify the model does not exist in the database
        self.assertNotIn(timetable, Timetable.objects.all())
