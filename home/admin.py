from django.contrib import admin
from .models import user, Datatable, Test_history
# Register your models here.

admin.site.register(user)
admin.site.register(Datatable)
admin.site.register(Test_history)
