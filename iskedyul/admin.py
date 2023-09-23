from django.contrib import admin

from iskedyul.models import Event, Timetable

# Register your models here.

admin.site.register(Timetable)
admin.site.register(Event)