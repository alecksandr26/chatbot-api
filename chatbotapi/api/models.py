from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Intent(models.Model):
    tagname = models.CharField(max_length = 50, null = False, unique = True)
    list_display = ["id", "tagname"]

    def __str__(self):
        return f"[tagname = {self.tagname}]"

class Pattern(models.Model):
    pattern = models.TextField(max_length = 500, null = False, unique = True)
    intent = models.ForeignKey(Intent, on_delete = models.CASCADE, null = False, related_name = "patterns")

    list_display = ["id", "pattern", "intent"]

    def __str__(self):
        return f"[pattern = {self.pattern}, intent = {self.intent}]"

class Answer(models.Model):
    answer = models.TextField(max_length = 500, null = False, unique = True)
    intent = models.ForeignKey(Intent, on_delete = models.CASCADE, null = False, related_name = "answers")

    list_display = ["id", "answer", "intent"]

    def __str__(self):
        return f"[answer = {self.answer}, intent = {self.intent}]"

