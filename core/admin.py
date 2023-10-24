from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.
admin.site.register(office)
admin.site.register(Status)
#admin.site.register(Labs_cabinets)
@admin.register(Application)
class ApplicationAdmin(SimpleHistoryAdmin):
    pass