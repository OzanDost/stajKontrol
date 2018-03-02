# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Entry(models.Model):
    name_of_company = models.CharField(max_length=200)
    name_of_student = models.CharField(max_length=200)