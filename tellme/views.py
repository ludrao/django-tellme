import json
from base64 import b64decode

from django.http import JsonResponse, HttpResponseBadRequest
from django.core.files.base import ContentFile
from tellme.forms import FeedbackForm


def post_feedback(request):

    if request.method == 'POST' and request.is_ajax():

        # Copy Post data names into names used into the model in order to automatically create the model/form
        # from the request dicts
        feedback = json.loads(request.POST["feedback"])
        data = {'url': feedback['url'], 'browser': json.dumps(feedback['browser']), 'comment': feedback['note'],
                'user': request.user.id}
        imgstr = feedback['img'].split(';base64,')[1]
        file = {'screenshot': ContentFile(b64decode(imgstr), name="screenshot.png")}
        form = FeedbackForm(data, file)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'error': dict(form.errors)})

    else:
        return HttpResponseBadRequest()
