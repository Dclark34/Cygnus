from django.contrib import admin

# Register your models here.
from .models import Sighting, Bird

admin.site.register(Sighting)
admin.site.register(Bird)