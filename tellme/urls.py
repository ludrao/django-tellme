from django.conf.urls import url

from .views import post_feedback


urlpatterns = [
    url(r'^$', post_feedback, name='post_feedback'),
]

