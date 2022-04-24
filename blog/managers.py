import django
from django.db import models
# from django.utils.timezone import timezone


class MyPostManager(models.Manager):
    def get_last_week_posts(self):
        from_date = django.utils.timezone.now() - django.utils.timezone.timedelta(days=7)
        to_date = django.utils.timezone.now()
        return super().get_queryset().filter(create_time__range=[from_date, to_date])


