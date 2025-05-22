from django.db import models
from django.contrib.auth.models import User
from utils.genearte_code import generate_code
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django_countries.fields import CountryField

ADDRESS_TYPE=[
    ('Home','Home'),
    ('Office','Office'),
    ('Others','Others')
              ]

class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo_user')
    code=models.CharField(max_length=75,default=generate_code)
    phone=models.CharField(max_length=25)
    address=models.ForeignKey('Address',related_name='profile_address',on_delete=models.SET_NULL,null=True,blank=True)
    join_at=models.DateTimeField(default=timezone.now)
    country = CountryField()


    def __str__(self):
        return str(self.user)
    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance

        )
    
class Address(models.Model):
    user=models.ForeignKey(User,related_name='address_user',on_delete=models.CASCADE)
    address=models.CharField(max_length=120)
    address_type=models.CharField(max_length=120,choices=ADDRESS_TYPE)




