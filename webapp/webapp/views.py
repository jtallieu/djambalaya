# Create your views here.
from django.http import HttpResponse

import logging
log = logging.getLogger('webapp')


def index_view(request):
    log.info('Handling index view: {}'.format(request))
    return HttpResponse("Welcome to DJAMBALAYA")
