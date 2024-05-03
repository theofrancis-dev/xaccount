from django.contrib import admin

# Register your models here.
from .models import BusinessType,Address,Person,Business


admin.site.register(BusinessType)
admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Business)