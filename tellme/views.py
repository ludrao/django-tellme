import json
from base64 import b64decode

from django.conf import settings
from django.core import urlresolvers
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
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
            f = form.save()

            if hasattr(settings, 'TELLME_FEEDBACK_EMAIL'):
                message = _("Your site %(host)s received feedback from %(user)s.\n"
                            "The comments were:\n"
                            "%(note)s.\n\n"
                            "See the full feedback content here: %(url)s")\
                          % {'host': request.get_host(), 'user': str(request.user), 'note': feedback['note'],
                             'url': request.build_absolute_uri(
                                 urlresolvers.reverse('admin:tellme_feedback_change', args=(f.id,)))}
                send_mail(
                        _('[%(host)s] Received feedback') % {'host': request.get_host()},
                        message,
                        settings.SERVER_EMAIL,
                        [settings.TELLME_FEEDBACK_EMAIL],
                        fail_silently=True)

            return JsonResponse({})
        else:
            return JsonResponse({'error': dict(form.errors)})

    else:
        return HttpResponseBadRequest()
