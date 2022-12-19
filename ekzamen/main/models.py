from datetime import datetime
from os.path import splitext

from django.db import models

from django.utils.crypto import get_random_string

from .utilities import get_timestamp_path


def get_name_file(instanse, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class Product(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    descriptions = models.TextField(verbose_name='описание', blank=True)
    photo_file = models.ImageField(max_length=254, upload_to=get_timestamp_path,
                                   blank=True, null=True)
