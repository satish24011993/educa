from django.db import models

class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created =models.DateTimeField(auto_now_add=True)

class Text(BaseContent):
    body = models.TextField()
