from django.db import models
from django.utils.translation import gettext_lazy as _

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
