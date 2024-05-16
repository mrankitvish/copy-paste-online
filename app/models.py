from django.db import models
import uuid

class Note(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()