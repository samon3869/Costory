from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name="Data Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Data Updated", auto_now=True)

    def __str__(self):
        return self.title