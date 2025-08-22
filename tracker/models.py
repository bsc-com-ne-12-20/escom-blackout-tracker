from django.db import models

# Create your models here.
class Groups_and_Area(models.Model):
    Group_ID = models.CharField(max_length=10)
    Region = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Affected_Areas = models.TextField()

    def __str__(self):
        return self.Group_ID

class BlackoutSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    groups = models.ManyToManyField(Groups_and_Area, related_name='schedules')

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"