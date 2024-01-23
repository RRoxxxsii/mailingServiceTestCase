from django.contrib import admin

from .db import models

admin.site.register(models.Client)
admin.site.register(models.Mailing)
admin.site.register(models.Message)
