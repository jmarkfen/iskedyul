from django.shortcuts import redirect, render
from django.urls import reverse
from iskedyul import presenters
from iskedyul.forms import EventForm, TimetableForm
from iskedyul.models import Event, Timetable

# Create your views here.


def create_timetable(request):
    template_name = "iskedyul/pages/create_timetable.html"
    context = {
        "form_action": reverse(save_timetable),
        "next_url": reverse(timetable_list),
    }
    return render(request, template_name, context)


def save_timetable(request):
    try:
        timetable = Timetable.objects.get(pk=request.POST.get("id"))
        form = TimetableForm(request.POST or None, instance=timetable)
    except:  # noqa: E722
        form = TimetableForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect(request.POST.get("next_url"))


def timetable_list(request):
    template_name = "iskedyul/pages/timetable_list.html"
    context = {"timetables": Timetable.objects.all()}
    return render(request, template_name, context)


def edit_timetable(request, timetable_id, event=None):
    template_name = "iskedyul/pages/edit_timetable.html"
    timetable = Timetable.objects.get(pk=timetable_id)
    context = {
        "form_action": reverse(save_timetable),
        "next_url": reverse(edit_timetable, kwargs={"timetable_id": timetable_id}),
        "timetable": timetable,
        "event": event,
        "table": presenters.TimetableViewer(timetable.events),
    }
    return render(request, template_name, context)


def delete_timetable_dialog(request, timetable_id):
    template_name = "iskedyul/pages/delete_timetable.html"
    context = {
        "form_action": reverse(delete_timetable),
        "timetable": Timetable.objects.get(pk=timetable_id),
        "ok_url": reverse(timetable_list),
        "cancel_url": reverse(edit_timetable, kwargs={"timetable_id": timetable_id}),
    }
    return render(request, template_name, context)


def delete_timetable(request):
    if request.POST.get("button_choice") == "ok":
        timetable = Timetable.objects.get(pk=request.POST.get("id"))
        timetable.delete()
        next_url = request.POST.get("ok_url")
    else:
        next_url = request.POST.get("cancel_url")
    return redirect(next_url)


def edit_event(request, timetable_id, id):
    event = Event.objects.get(timetable_id=timetable_id, pk=id)
    return edit_timetable(request, timetable_id, event)


def delete_event_dialog(request, timetable_id, event_id):
    template_name = "iskedyul/pages/delete_event.html"
    event = Event.objects.get(pk=event_id)
    timetable = Timetable.objects.get(pk=timetable_id)
    context = {
        "event": event,
        "ok_url": reverse(edit_timetable, kwargs={
            "timetable_id": timetable_id,
        }),
        "cancel_url": reverse(edit_event, kwargs={
            "timetable_id": timetable_id, 
            "id": event.id,
        }),
        "timetable": timetable,
        "table": presenters.TimetableViewer(timetable.events),
    }
    return render(request, template_name, context)
