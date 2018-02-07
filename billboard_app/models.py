# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    user_name = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    text = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title

    
