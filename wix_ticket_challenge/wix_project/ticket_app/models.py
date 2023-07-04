from django.db import models


class Ticket(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    userEmail = models.EmailField()
    creationTime = models.DateTimeField()
    labels = models.JSONField(null=True)

    def __str__(self):
        return self.title
