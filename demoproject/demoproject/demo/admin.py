from django.contrib import admin
from .models import places
from .models import peoples

# Register your models here.
admin.site.register(places)
admin.site.register(peoples)