import django

try:
    from django.urls import path, include
except ImportError:
    from django.conf.urls import url, include


from .views import post_feedback


if django.VERSION[0] < 2:
    tellme_urlpatterns = [
        url(r'^post_feedback/$', post_feedback, name='post_feedback'),
    ]

    urlpatterns = [
        url(r'^', include(tellme_urlpatterns,
            namespace='tellme')),
    ]
else:
    tellme_urlpatterns = [
        path('post_feedback/', post_feedback, name='post_feedback'),
    ]

    app_name = 'tellme'

    urlpatterns = [
        path('', include(tellme_urlpatterns,)),
    ]
