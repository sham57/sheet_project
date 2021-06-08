from django.contrib import admin

# Register your models here.
from . models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('listing',"listing_id","name","contact_date","email")
    list_display_links = ('listing_id',"name")
    search_fields = ("name","email","listing")
    list_per_page = 4
admin.site.register(Contact, ContactAdmin)
