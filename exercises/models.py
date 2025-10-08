from django.db import models

# Create your models here.


class Exercise(models.Model):
    EXERCISE_TYPE = [
        ('WARM', 'Warm Up'),
        ('SCAL', 'Scales'),
        ('SONG', 'Song Training'),
        ('TECH', 'Technique'),
        ('OTHE', 'Other'),
    ]

    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=4, choices=EXERCISE_TYPE)
    description = models.TextField()
    time = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_type_display()} ({self.time} min) - {self.date}"