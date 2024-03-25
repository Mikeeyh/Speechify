from django.shortcuts import render
from Speechify.profiles.models import Profile


def index(request):
    if request.user.is_authenticated:
        template_name = 'web/home-with-profile.html'
    else:
        template_name = 'base.html'

    context = {
        'user': request.user,
    }

    return render(request, template_name, context)


# # views.py
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404
