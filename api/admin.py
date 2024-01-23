from django.contrib import admin
from .models import Churras


@admin.register(Churras)
class ChurrasAdmin(admin.ModelAdmin):
    ...
