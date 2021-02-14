from django.db import models

class Projects(models.Model):
    Name=models.TextField(max_length=60,null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)
    link =models.URLField(null=True,blank=True)

    def __str__(self):
        return self.Name;

