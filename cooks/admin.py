from django.contrib import admin
from waiters.models import waiterprofile
from cooks.models import cookprofile

admin.site.register(waiterprofile)
admin.site.register(cookprofile)


