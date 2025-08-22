from django.db import models

# Create your models here.
class Groups_and_Area(models.Model):
    Group_ID = models.CharField(max_length=10)
    Region = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Affected_Areas = models.TextField()

    def __str__(self):
        return self.Group_ID

# class Blackout_Schedule(models.Model):
#     Schedule_ID = models.CharField(max_length=10, primary_key=True)
#     Group = models.ForeignKey(Groups_and_Area, on_delete=models.CASCADE)
#     Start_Time = models.DateTimeField()
#     End_Time = models.DateTimeField()

#     def __str__(self):
#         return self.Schedule_ID