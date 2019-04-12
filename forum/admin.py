from django.contrib import admin

# Register your models here.
from .models import thread
from .models import comment
from .models import resource
admin.site.register(thread),
admin.site.register(comment)
admin.site.register(resource)



