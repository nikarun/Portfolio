from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50,null=True)
    pub_date=models.DateField(null=True,blank=True)
    body=models.TextField(max_length=400,null=True)
    image=models.ImageField(null=True,blank=True)

    # def __str__(self):
    #     return self.title

    def summary(self):
        return self.body[:100];

