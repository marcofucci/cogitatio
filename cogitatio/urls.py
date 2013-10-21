# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^auth/', include('auth.urls')),

    url(r'^idea/', include('idea.urls', namespace='idea')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="home.html")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
