from django.db import models
from userprofile.models import UserProfile


class Exercise(models.Model):
    EXERCISE_TYPE = [
        ('WARM', 'Warm Up'),
        ('SCAL', 'Scales'),
        ('SONG', 'Song Training'),
        ('TECH', 'Technique'),
        ('OTHE', 'Other'),
    ]

    user_profile = models.ForeignKey(
        "userprofile.UserProfile",
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=4, choices=EXERCISE_TYPE)
    description = models.TextField()
    time = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_type_display()} ({self.time} min) - {self.date}"