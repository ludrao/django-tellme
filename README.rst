
.. image:: https://img.shields.io/pypi/v/django-tellme.svg
    :target: https://pypi.python.org/pypi/django-tellme/

.. image:: https://img.shields.io/github/license/ludrao/django-tellme.svg 
    :target: https://en.wikipedia.org/wiki/BSD_licenses

======
tellme
======

tellme is a simple Django app that provides an easy and simple feedback button, form and admin view.

Features
--------

* Take a screenshot of the current page.
* The user can then highlight or black out portions of that screenshot
* The user can then provide textual comments, (effectively giving his feedback)
* Some additional information collected with the feedback
    * various browser information (versions, user agent, etc.)
    * user information if the user is logged in (and your site uses Django auth system)
    * the url the user provides feedback on
* Optionally, send an email to the site admin when a feedback is posted

The javascript part of this app is using feedback.js from https://github.com/ivoviz/feedback.
feedback.js itself use html2canvas.js (https://github.com/niklasvh/html2canvas) to make page screenshot that is sent
with the feedback comments.

Dependencies
------------

This application depends on
    - python 3 (might work on python 2, but untested)
    - django >= 1.8
    - jquery must be enabled in your pages


Quick start
-----------

0. Install the app in your environment:

.. code:: bash

    pip install django-tellme


1. Add "tellme" to your INSTALLED_APPS setting like this:

.. code:: python

    INSTALLED_APPS = [
        ...
        'tellme',
    ]

2. Include the tellme URLconf in your project urls.py like this:

.. code:: python

    url(r'^tellme/', include("tellme.urls", namespace="tellme")),


3. Run ``python manage.py migrate`` to create the tellme model in the database.

4. Add a feedback button in your pages so that user can provide feedback

For example using bootstrap CSS this code would overlay a button, vertically aligned on the middle of the
page, right-aligned.

In your html/template file, import the form CSS:

.. code:: html

    <link href="{% static 'tellme/feedback.css' %}" rel="stylesheet">

In your html/template file, inside the <body> section:

.. code:: html

    <button type="button" id="feedback-btn" class="btn btn-info vertical-right-aligned">
        Feedback <span class="glyphicon glyphicon-bullhorn" aria-hidden="true"></span>
    </button>

Note: the CSS class vertical-right-aligned is not from bootstrap, it is defined as:

.. code:: css

    .vertical-right-aligned {
        transform: rotate(-90deg);
        transform-origin: 100% 100%;
        position: fixed;
        right: 0;
        top: 50%;
        z-index: 100;
    }

In your html/template file, in the page footer, connect that button to the feedback plugin:

.. code:: html

    <script src="{% static 'tellme/feedback.js' %}"></script>
    <script type="text/javascript">
        $(function () {
            $.feedback({
                ajaxURL: {% url 'tellme:post_feedback' %},
                html2canvasURL: "{% static 'tellme/html2canvas.min.js' %}",
                feedbackButton: "#feedback-btn",
                postHTML: false,
                onClose: function() { window.location.reload(); }
            });
        });
    </script>


5. Start your site, and click the feedback button. This will pop up the feedback form. Follow the instruction, and click on **Send** when finished.


6. Visit http://127.0.0.1:8000/admin/ to review user feedback.


Email notifications
-------------------

This app can send you an email every time a feedback is posted. Currently the email is plaintext and does not contain
the screenshot. However it does contain a link to the admin site with the full details of that feedback.

To enable email notification, just add this line in your site ``settings.py``:

  .. code:: python

    TELLME_FEEDBACK_EMAIL = 'admin@tellme.com'



Important Notes
---------------

.. note::

    This app is based on feedback.js that send the feedback content using an HTTP POST method. Django uses a CSRF protection
    mechanism, that block POST request that do not contain a specific token.
    If you have not setup your page to transparently support AJAX POST here is an explanation on how to do it:
    https://docs.djangoproject.com/en/1.8/ref/csrf/#ajax

.. note::

    This app stores screenshot as part of the feedback. Those are stored as PNG image files into your MEDIA
    directory/backend.
    For this reason you need to have MEDIA_URL and MEDIA_ROOT settings available. See here for more details:
    https://docs.djangoproject.com/en/1.8/howto/static-files/

.. note::

    If using the email notification feature, make sure to setup your Email backend in django. More details here:
    https://docs.djangoproject.com/en/1.8/topics/email/


Improving this app - TODO
-------------------------

This app was developed in rush for a simple yet complete, non intrusive, feedback tool. It does lack a lot of cool
features. If you like to contribute, please do not hesitate!

- Provide a customization mechanism for the feedback popup/form.
- Provide a customization mechanism for the email body, make it text+html.
- Implement internationalization (i18n).

