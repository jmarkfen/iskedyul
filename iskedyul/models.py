from django.db import models
from django.utils.translation import gettext_lazy as _

from iskedyul import querysets

# Create your models here.


class Timetable(models.Model):
    """Model definition for Timetable."""

    title = models.CharField(_("title"), max_length=50)

    class Meta:
        """Meta definition for Timetable."""

        verbose_name = "Timetable"
        verbose_name_plural = "Timetables"

    def __str__(self):
        """Unicode representation of Timetable."""
        return self.title


class Days(models.IntegerChoices):
    MONDAY = 1, _("Monday")
    TUESDAY = 2, _("Tuesday")
    WEDNESDAY = 3, _("Wednesday")
    THURSDAY = 4, _("Thursday")
    FRIDAY = 5, _("Friday")
    SATURDAY = 6, _("Saturday")
    SUNDAY = 7, _("Sunday")


class Event(models.Model):
    """Model definition for Event."""

    timetable = models.ForeignKey(
        Timetable,
        verbose_name=_("timetable"),
        on_delete=models.CASCADE,
        related_name="events",
    )
    text = models.TextField(_("text"))
    day = models.IntegerField(_("day"), choices=Days.choices)
    start_time = models.TimeField(_("start time"))
    end_time = models.TimeField(_("end time"))

    objects = querysets.EventQuerySet.as_manager()

    class Meta:
        """Meta definition for Event."""

        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        """Unicode representation of Event."""
        return self.timetable.title + " - (" + Days(self.day).label + ") " + self.text
