from django.db import models


class EventQuerySet(models.QuerySet):
    def where_day(self, day):
        """
        filter by day, sorted by start time
        """
        return self.filter(day=day).order_by("start_time")

    def group_by_days(self, days):
        """
        return dict of day as keys, groups as values
        """
        groups = {}
        for day in days:
            group = self.where_day(day)
            groups[day] = group
        return groups
