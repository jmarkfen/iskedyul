from django.urls import path

from iskedyul import forms, views

urlpatterns = [
    path("timetables/new/", views.create_timetable, name="create_timetable"),
    path("timetables/save/", views.save_timetable, name="save_timetable"),
    path("timetables/", views.timetable_list, name="timetable_list"),
    path("timetables/<int:timetable_id>/", views.edit_timetable, name="edit_timetable"),
    path("timetables/<int:timetable_id>/delete/", views.delete_timetable_dialog, name="delete_timetable_dialog"),
    path("timetables/delete/", views.delete_timetable, name="delete_timetable"),

    path("events/save/", forms.save_event, name="save_event"),
    path(
        "timetable/<int:timetable_id>/events/<int:id>/", 
        views.edit_event, name="edit_event",
    ),
    path(
        "timetables/<int:timetable_id>/events/<int:event_id>/delete", 
        views.delete_event_dialog, 
        name="delete_event_dialog"
    ),
    path("events/delete/", forms.delete_event, name="delete_event"),
    
]
