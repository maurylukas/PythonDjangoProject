from django.db import models
from django.utils import timezone

# Create your models here.

LIST = (
    ('Analises', 'Análises'),
    ('Programacao', 'Programação'),
    ('Apresentacao', 'Apresentação'),
    ('Outros', 'Outros'),
)


class Serie (models.Model):
    title = models.CharField (max_length = 100)
    icon = models.ImageField (upload_to = 'icons')
    description = models.TextField (max_length = 1000)
    category = models.CharField (max_length = 15, choices = LIST)
    views = models.IntegerField (default = 0)
    date = models.DateTimeField (default = timezone.now)

    def __str__(self):
        return self.title