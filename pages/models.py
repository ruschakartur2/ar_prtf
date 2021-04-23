from django.db import models


# Create your models here.
from django.urls import reverse


class Work(models.Model):
    title = models.CharField(max_length=255, verbose_name='name of project')
    description = models.TextField(verbose_name='Description of project')
    demo_link = models.CharField(max_length=255, verbose_name='Link to project', blank=True)
    source_link = models.CharField(max_length=255, verbose_name='Link to source code', blank=True)
    technologies_used = models.CharField(max_length=255, verbose_name='Technologies used in project')
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])