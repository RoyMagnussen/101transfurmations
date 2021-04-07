from django.db import models
from datetime import datetime

# Create your models here.


class Review(models.Model):
    name = models.CharField(verbose_name='Customer Name',
                            max_length=255, default='A 101 Transfurmations Customer', help_text='255 characters or less.')
    comment = models.TextField(
        verbose_name='Comment', max_length=2000, help_text='2000 characters or less.')
    date_added = models.DateTimeField(
        verbose_name='Date Added', default=datetime.utcnow, help_text='The date and time the review was created.')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self) -> str:
        return f'{self.name}-{self.date_added}'
