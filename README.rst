=====
tellme
=====

tellme is a simple Django app that provides an easy and simple feedback button, form and admin view.

Features
--------
    * Take a screenshot of the current page.
    * The user can then highlight or black out portions of that screenshot
    * The user can then provide textual comments, (effectively giving his feedback)
    * Some additional information collected with the feedback:
        * various browser information (versions, user agent, etc.)
        * user information if the user is logged in (and your site uses Django auth system)
        * the url the user provides feedback on

The javascript part of this app is using feedback.js from https://github.com/ivoviz/feedback.
feedback.js itself use html2canvas.js (https://github.com/niklasvh/html2canvas) to make page screenshot that is sent
with the feedback comments.

Dependencies
------------

This application depends on:
    python 3 (might work on python 2, but untested)
    django >= 1.8
    jquery must be enabled in your pages


Quick start
-----------

1. Add "tellme" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'tellme',
    ]

2. Include the tellme URLconf in your project urls.py like this::

    url(r'^tellme/', include("tellme.urls", namespace="tellme")),

3. Run `python manage.py migrate` to create the tellme models.

4. Add a feedback button in your pages so that user can provide feedback

    For example using bootstrap CSS this code would overlay a button, vertically aligned on the middle of the
    page, right-aligned.

        In your html/template file, import the form CSS:
            <link href="{% static 'tellme/feedback.css' %}" rel="stylesheet">

        In your html/template file, inside the <body> section:
            <button type="button" id="feedback-btn" class="btn btn-info vertical-right-aligned">Feedback
            <span class="glyphicon glyphicon-bullhorn" aria-hidden="true"></span>
            </button>

            Note: CSS class vertical-right-aligned is not from bootstrap, it is defined as:
                .vertical-right-aligned {
                    transform: rotate(-90deg);
                    transform-origin: 100% 100%;
                    position: fixed;
                    right: 0;
                    top: 50%;
                    z-index: 100;
                }

        In your html/template file, in the page footer, connect that button to the feedback plugin:
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


5. Start your site, and click the feedback button. This will pop up the feedback form. Follow the instruction, and
    click on Send when finished.


6. Visit http://127.0.0.1:8000/admin/ to review user feedback.