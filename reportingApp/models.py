from django.db import models


class Store(models.Model):
    store_id = models.BigIntegerField(primary_key=True)
    timezone_str = models.CharField(max_length=200, null=False, blank=False, default="America/Chicago")

    def __str__(self):
        return self.store_id


class BusinessHour(models.Model):
    DAYS = [
        (0, "MONDAY"),
        (1, "TUESDAY"),
        (2, "WEDNESDAY"),
        (3, "THURSDAY"),
        (4, "FRIDAY"),
        (5, "SATURDAY"),
        (6, "SUNDAY"),
    ]
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAYS)
    start_time_local = models.DateTimeField()
    end_time_local = models.DateTimeField()


class Status(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Status"
