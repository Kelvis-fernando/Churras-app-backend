from django.db import models
from django.contrib.auth.models import User


class Churras(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    image = models.ImageField(upload_to='churras_images/')
    address = models.CharField(max_length=165)
    items = models.JSONField()
    participantes = models.ManyToManyField(
        User, related_name='churras_participations')

    def __str__(self):
        return self.title if self.title else str(self.pk)
