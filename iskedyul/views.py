from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from iskedyul.forms import TimetableForm

# Create your views here.

def create_timetable(request):
    template_name = "iskedyul/pages/create_timetable.html"
    context = {
        "form_action": reverse(save_timetable),
        "next_url": reverse(create_timetable),
    }
    return render(request, template_name, context)

def save_timetable(request):
    form = TimetableForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(request.POST.get("next_url"))
