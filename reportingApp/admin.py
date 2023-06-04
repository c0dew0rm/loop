from django.contrib import admin

from .models import *


class StoreAdmin(admin.ModelAdmin):
    fields = []


class BusinessHourAdmin(admin.ModelAdmin):
    fields = []


class StatusAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(Store, StoreAdmin)
admin.site.register(BusinessHour, StoreAdmin)
admin.site.register(Status, StoreAdmin)
