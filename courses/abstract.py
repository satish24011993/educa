from django.db import models

class BaseContent(models.Model):
    title = models.CharField(max_lenght=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Text(BaseContent):
    body = models.TextField()