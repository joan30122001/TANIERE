from django.contrib import admin
from .models import Landing



class LandingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')



admin.site.register(Landing, LandingAdmin)