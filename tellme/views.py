import json
from base64 import b64decode

from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string

from tellme.forms import FeedbackForm
from tellme.mail import send_mail


def post_feedback(request):
    if request.method == 'POST' and request.is_ajax():

        # Copy Post data names into names used into the model in order to automatically create the model/form
        # from the request dicts
        feedback = json.loads(request.POST["feedback"])
        if request.user.id:
            data = {'url': feedback['url'], 'browser': json.dumps(feedback['browser']), 'comment': feedback['note'],
                        'user': request.user.id}
        else:
            data = {'url': feedback['url'], 'browser': json.dumps(feedback['browser']), 'comment': feedback['note'],
                        'email': feedback.get('email')}
        imgstr = feedback['img'].split(';base64,')[1]
        file = {'screenshot': ContentFile(b64decode(imgstr), name="screenshot_" + get_random_string(6) + ".png")}
        form = FeedbackForm(data, file)
        # check whether it's valid:
        if form.is_valid():
            f = form.save()

            if hasattr(settings, 'TELLME_FEEDBACK_EMAIL'):
                send_mail(request, f)
            return JsonResponse({})
        else:
            return JsonResponse({'error': dict(form.errors)})

    else:
        return HttpResponseBadRequest()
