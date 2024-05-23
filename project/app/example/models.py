from django.db import models

class URLVisit(models.Model):
    url = models.CharField(max_length=255, unique=True)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url