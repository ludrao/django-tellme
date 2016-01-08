from django.conf import settings
from django.db import models


# Create your models here.
class Feedback(models.Model):
    url = models.CharField(max_length=255)
    browser = models.TextField()
    comment = models.TextField()
    screenshot = models.ImageField(blank=True, null=True, upload_to="tellme/screenshots/")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


# Receive the post_delete signal and delete the file associated with the model instance.
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


@receiver(post_delete, sender=Feedback)
def feedback_screenshot_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.screenshot:
        instance.screenshot.delete(save=False)