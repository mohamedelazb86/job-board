from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

JOP_TYPE=[
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
          ]
class Job(models.Model):
    user=models.ForeignKey(User,related_name='job_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    jop_type=models.CharField(max_length=75,choices=JOP_TYPE)
    descriptions=models.TextField(max_length=2500)
    publish_date=models.DateTimeField(default=timezone.now)
    vacancy=models.IntegerField(default=1)
    salary=models.FloatField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',related_name='job_category',on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(upload_to='image_job',null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    loction=models.ForeignKey('Loction',related_name='job_loction',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)


class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Loction(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)


    def __str__(self):
        return self.name
class Apply(models.Model):
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,related_name='apply_user',on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    website=models.URLField(null=True,blank=True)
    cv=models.FileField(upload_to='cv')
    content=models.TextField(max_length=1500)
    image=models.ImageField(upload_to='image_eng')

    def __str__(self):
        return self.name
    