from PIL import Image
from django.db import models

# Create your models here.


class GalleryImage(models.Model):
    name = models.CharField(
        verbose_name='Name', max_length=255, help_text='255 characters or less.')
    image = models.ImageField(verbose_name='Image', upload_to='gallery_images')

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):

        img = Image.open(self.image)
        img.thumbnail((300, 500))
        img.save(self.image)
        
        super(GalleryImage, self).save(*args, **kwargs)
