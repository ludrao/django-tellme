from django.test import TestCase
from tellme.models import Feedback
from tellme.tests.factories import FeedbackFactory


class FeedbackScreenshotDeleteTest(TestCase):
    def test_signal(self):
        feedback = FeedbackFactory()
        self.assertTrue(feedback.screenshot)
        feedback.delete()
        self.assertFalse(feedback.screenshot)
