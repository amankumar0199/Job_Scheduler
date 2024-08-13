from django.db import models

from django.utils import timezone
import datetime


# Create your models here.
class Job(models.Model):
    JOB_TYPE = [
        ('email', 'email notification'),
        ('crunch', 'number crunching')
    ]

    name = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    schedule_interval = models.DurationField()
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.next_run:
            self.next_run = timezone.now() + self.schedule_interval
        super().save(*args, **kwargs)

    def should_run(self):
        return timezone.now() >= self.next_run

    def update_next_run(self):
        self.last_run = timezone.now()
        self.next_run = timezone.now() + self.schedule_interval
        self.save()



    def __str__(self):
        return self.name
