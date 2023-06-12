from datetime import timezone
from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

def upload_location(instance, filename, **kwargs):
    file_path = 'video/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path

class Post (models.Model):
    title               =models.CharField(max_length=50,null=False, blank=False)
    image               =models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published      =models.DateTimeField(auto_now_add=True, verbose_name='date pub')
    date_updated        =models.DateTimeField(auto_now=True, verbose_name='date updated')
    author              =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug                =models.SlugField(blank=True, unique=True)
    video               =models.FileField(upload_to=upload_location, null=False,default="")
    tanctipus           =models.TextField(max_length=100,null=False,blank=False,default="")
    hely                =models.TextField(max_length=100,null=False,blank=False,default="")
    datum               =models.DateField(blank=False,null=False,default="2023-01-01")
    tancos              =models.TextField(max_length=100,null=False,blank=False,default="")
    def __str__(self):
        return self.title  

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)      

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + instance.title)

pre_save.connect(pre_save_post_reciever, sender=Post)


