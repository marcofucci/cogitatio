from django.conf.urls import patterns, url

from allauth.socialaccount.providers.github import views as gh_views
from allauth.account import views as account_views

urlpatterns = patterns('',
    url(r'^login/$', gh_views.oauth2_login, name="github_login"),
    url(r'^github/callback/$', gh_views.oauth2_callback, name="github_callback"),
    url(r"^logout/$", account_views.logout, name="account_logout"),
)
