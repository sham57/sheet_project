from django.contrib import admin
from .models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id","name","email")
    list_display_links = ("id","name")
    search_fields = ("id","name")
    list_per_page = 2

admin.site.register(Realtor, RealtorAdmin)
# Register your models here.
