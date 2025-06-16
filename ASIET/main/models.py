from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('department_detail', args=[str(self.id)])

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


    def __str__(self):
        return self.title