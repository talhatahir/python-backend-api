from django.contrib import admin
from .models import listings,images,users

admin.site.register(images)
admin.site.register(users)
admin.site.register(listings)
