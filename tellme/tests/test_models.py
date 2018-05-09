from django.test import TestCase
from tellme.models import Feedback
from tellme.tests.factories import FeedbackFactory


class FeedbackScreenshotDeleteTest(TestCase):
    def test_delete_screenshot(self):
        feedback = FeedbackFactory()
        self.assertTrue(feedback.screenshot)
        feedback.delete()
        self.assertFalse(feedback.screenshot)

    def test_no_screenshot(self):
        feedback = FeedbackFactory(screenshot=None)
        feedback.delete()
        self.assertFalse(feedback.screenshot)
