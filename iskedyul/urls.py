from django.urls import path

from iskedyul import views

urlpatterns = [
    path("timetables/new/", views.create_timetable, name="create_timetable"),
    path("timetables/save/", views.save_timetable, name="save_timetable"),
    path("timetables/", views.timetable_list, name="timetable_list"),
    path("timetables/<int:timetable_id>/", views.edit_timetable, name="edit_timetable"),
]
