from django.contrib import admin

# Register your models here.

from .models import pd1_time
from .models import pd2

admin.site.register(pd1_time)
admin.site.register(pd2)
