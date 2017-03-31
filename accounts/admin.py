from django.contrib import admin

# Register your models here.
from .models import Akcija, Profile, Komentar


admin.site.register(Akcija)
admin.site.register(Profile)
admin.site.register(Komentar)
