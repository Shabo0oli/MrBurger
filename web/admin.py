# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

class AnswerAdmin(admin.ModelAdmin):
    list_filter = (
        ('Date', JDateFieldListFilter),
    )

admin.site.register(Answer, AnswerAdmin )