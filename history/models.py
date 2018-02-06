from django.db import models
from simple_history.models import HistoricalRecords

class Publication(models.Model):
    title = models.CharField(max_length=30)
    history = HistoricalRecords()
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    history = HistoricalRecords(many_to_many_fields=['publications'])

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
