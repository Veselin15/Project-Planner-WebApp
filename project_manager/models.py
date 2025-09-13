from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Expected URL name: 'project-detail' with pk argument.
        Update the reverse() target here if your URL name is different.
        """
        return reverse('project_detail', args=[self.pk])
class Plan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='plans')
    name = models.CharField(max_length=255)
    content =  RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('project', 'name'),)
        ordering = ['created_at']

    def __str__(self):
        return f"{self.project.name} - {self.name}"
