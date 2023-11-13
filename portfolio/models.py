from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    link = models.URLField(null=True, blank=True),
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of update")
   
class Meta:
        ordering = ["created"]

def __str__(self):
        return self.title

