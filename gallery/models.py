import itertools
import os
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_delete
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Photo(models.Model):
    owner = models.CharField(max_length=50)

    title = models.CharField(max_length=50)

    slug = models.SlugField(max_length=25, unique=True)

    category = models.ManyToManyField(Category)

    date_created = models.DateField(default=timezone.now, editable=False)

    image = models.ImageField(upload_to="photos")

    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60}
                               )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self, model_name):
        return reverse('%s.views.details' % model_name, args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
            for x in itertools.count(1):
                if not Photo.objects.filter(slug=self.slug).exists():
                    break
            self.slug = slugify("%s-%d" % (self.title, x))
        super(Photo, self).save(*args, **kwargs)


def remove_photos_cache(sender, instance, **kwargs):
    global logger
    try:
        tnpath = instance.thumbnail.path
        os.remove(instance.image.path)
        os.remove(tnpath)
        os.removedirs(os.path.dirname(tnpath))
    except Exception:
        logger.error('Failed to clear image cache', exc_info=True)
post_delete.connect(remove_photos_cache, sender=Photo)
