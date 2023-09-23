from django import forms
from django.shortcuts import redirect
from .models import Timetable, Event


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ["title"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["timetable", "text", "day", "start_time", "end_time"]


def save_event(request):
    try:
        event = Event.objects.get(pk=request.POST.get("id"))
        form = EventForm(request.POST or None, instance=event)
    except:  # noqa: E722
        form = EventForm(request.POST or None)
        print(request.POST)
    if form.is_valid():
        form.save()
    return redirect(request.POST.get("next_url"))


def delete_event(request):
    if request.POST.get("button_choice") == "ok":
        event = Event.objects.get(pk=request.POST.get("id"))
        event.delete()
        return redirect(request.POST.get("ok_url"))
    else:
        return redirect(request.POST.get("cancel_url"))
