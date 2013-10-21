from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel


class Idea(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)

    def __unicode__(self):
        return u'%s' % self.title
