from django.conf.urls import patterns, url

from .views import AddIdeaView

urlpatterns = patterns('',
    url(r'^add/$', AddIdeaView.as_view(), name="add"),
)
