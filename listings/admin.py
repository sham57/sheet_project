from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title","is_published","list_date","realtor","price")
    list_display_links = ("id","title")
    list_filter = ("realtor",)
    list_editable = ("is_published",)
    search_fields = ("tile","city","state","zipcode","price")
    list_per_page = 2
admin.site.register(Listing, ListingAdmin)

# Register your models here.
