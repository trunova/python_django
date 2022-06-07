from django.contrib import admin
from advertisements_app.models import Advertisement, AdvertisementAuthor, AdvertisementSection

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

@admin.register(AdvertisementAuthor)
class AdvertisementAuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(AdvertisementSection)
class AdvertisementSectionAdmin(admin.ModelAdmin):
    pass