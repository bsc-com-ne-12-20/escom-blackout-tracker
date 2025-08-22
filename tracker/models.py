from django.db import models

# Create your models here.
class LoadSheddingGroup(models.Model):
    """Represents a load shedding group (A, A1, A2, B, B1, etc.)"""
    group_id = models.CharField(max_length=10, unique=True, primary_key=True)
    
    def __str__(self):
        return self.group_id

class GroupLocation(models.Model):
    """Represents specific locations within a group"""
    group = models.ForeignKey(LoadSheddingGroup, on_delete=models.CASCADE, related_name='locations')
    region = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    affected_areas = models.TextField()

    def __str__(self):
        return f"{self.group.group_id} - {self.location}"

class BlackoutSchedule(models.Model):
    """Represents blackout schedules for groups"""
    group = models.ForeignKey(LoadSheddingGroup, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.group.group_id} - {self.date} {self.start_time}-{self.end_time}"