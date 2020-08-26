from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=80,
        unique=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title
