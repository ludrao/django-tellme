from django.contrib.staticfiles import finders
from django.test import TestCase


MISSING_ASSET = 'Frontend asset missing. Did you build it?'


class AssetTests(TestCase):
    def test_finders_feedbackjs(self):
        result = finders.find('tellme/feedback/dist/feedback.js')
        self.assertTrue(result, MISSING_ASSET
    
    def test_finders_feedbackcss(self):
        result = finders.find('tellme/feedback/dist/feedback.css')
        self.assertTrue(result, MISSING_ASSET)
