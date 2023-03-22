from django.contrib import admin
from advertisement.models import *


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategory)
class AdvertisementCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementStatus)
class AdvertisementStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
