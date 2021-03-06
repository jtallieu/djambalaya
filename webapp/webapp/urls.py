"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from views import index_view, show_content
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^videobank', include('videobank.urls')),
    url(r'^api/v2/hollabacks/', include('stefani.urls')),
    url(r'^adminator$', RedirectView.as_view(url='/static/Adminator-admin-dashboard/build/index.html', permanent=False)),
    url(r'^adminLTE$', RedirectView.as_view(url='/static/AdminLTE/index.html', permanent=False)),
    url(r'^djamba/(?P<content_path>.+?)$', show_content),
    url(r'^$', index_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
