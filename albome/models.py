from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField('название', max_length=100, blank=True, default='')
    slug = models.SlugField('Транслит', max_length=150, null=True)
    image = models.ImageField('изображение', upload_to="albome/photos")
    date = models.DateTimeField()

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['title']

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, verbose_name='альбом', related_name='photos')
    image = models.ImageField('изображение', upload_to="albome/photos")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ['album']