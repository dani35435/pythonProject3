from django.contrib import admin
from main.models import *

from .models import Product

admin.site.register(Product)

