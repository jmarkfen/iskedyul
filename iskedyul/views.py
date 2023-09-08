from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from iskedyul.forms import TimetableForm
from iskedyul.models import Timetable

# Create your views here.

def create_timetable(request):
    template_name = "iskedyul/pages/create_timetable.html"
    context = {
        "form_action": reverse(save_timetable),
        "next_url": reverse(timetable_list),
    }
    return render(request, template_name, context)

def save_timetable(request):
    form = TimetableForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(request.POST.get("next_url"))

def timetable_list(request):
    template_name = "iskedyul/pages/timetable_list.html"
    context = {
        "timetables": Timetable.objects.all()
    }
    return render(request, template_name, context)

def edit_timetable(request, timetable_id):
    template_name = "iskedyul/pages/edit_timetable.html"
    context = {
        "form_action": reverse(save_timetable),
        "next_url": reverse(edit_timetable, kwargs={"timetable_id": timetable_id}),
        "timetable": Timetable.objects.get(pk=timetable_id)
    }
    return render(request, template_name, context)
