from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    is_naeb = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.is_naeb}"
