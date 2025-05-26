from django.db import models

class Setting(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='images')
    subtitle=models.TextField(max_length=2500)
    phone=models.CharField(max_length=25)
    email=models.CharField(max_length=120)
    address=models.CharField(max_length=130)
    facebook=models.URLField(null=True,blank=True)
    googleapp=models.URLField(null=True,blank=True)
    twitter=models.URLField(null=True,blank=True)
    instagram=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

