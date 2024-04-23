from django.contrib import admin

from .models import *

# Register your models here.

# Already registered
# admin.site.register(User)


@admin.register(Intent)
class IntentAdmin(admin.ModelAdmin):
    list_display = ["id", "tagname"]

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ["id", "pattern", "intent"]

@admin.register(Answer)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ["id", "answer", "intent"]



