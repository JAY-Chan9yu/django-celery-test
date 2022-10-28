from django.db import models


class Post(models.Model):
    content = models.TextField(max_length=500)
