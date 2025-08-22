from django.contrib import admin
from .models import LoadSheddingGroup, GroupLocation, BlackoutSchedule

# Register your models here.
admin.site.register(LoadSheddingGroup)
admin.site.register(GroupLocation)
admin.site.register(BlackoutSchedule)