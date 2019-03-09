from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^docs', include('rest_framework_docs.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
