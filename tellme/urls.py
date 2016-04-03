from django.conf.urls import url, include
from django.views.i18n import javascript_catalog

from .views import post_feedback


tellme_urlpatterns = [
    url(r'^post_feedback/$', post_feedback, name='post_feedback'),
]

urlpatterns = [
    url(r'^', include(tellme_urlpatterns, namespace="tellme")),
    ]
