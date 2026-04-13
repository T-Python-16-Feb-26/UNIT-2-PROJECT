from django.db import models

class CultureFact(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.topic