from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)


    def __unicode__(self):
        return self.name


class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='django_snippets')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    desciption = models.TextField(blank=True, null=True)
    snippet = models.TextField(blank=False, null=False)
    lenguage = models.ForeignKey(Language, on_delete=models.CASCADE, blank=False)
    public = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name + ' - ' + self.lenguage
