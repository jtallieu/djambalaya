# Create your views here.
from django.http import HttpResponse

import logging
log = logging.getLogger('stefani.webapp')


def index_view(request):
    log.info('Handling index view: {}'.format(request))
    return HttpResponse("Welcome to DJAMBALAYA")
