# Create your views here.
from django.shortcuts import render
import logging
log = logging.getLogger('webapp')


def index_view(request):
    log.info('Handling index view: {}'.format(request))
    return render(request, 'djamba/home.html')


def show_content(request, content_path):
    log.critical("Handling path {}".format(content_path))
    return render(request, "djamba/{}.html".format(content_path))
