from django.contrib import admin

# Register your models here.

from .models import Department, Room, Doctor, Medicine, Patient

admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Patient)

