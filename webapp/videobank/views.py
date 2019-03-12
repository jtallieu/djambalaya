# Create your views here.
from django.shortcuts import render

import logging
log = logging.getLogger('videobank.webapp')


def main(request):
    log.info('Handling index view: {}'.format(request))
    return render(request, "vms/home.html")
