from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from django.contrib.auth import get_user_model
from django import template
from groups.models import Group
from uuid import uuid4
import os

User = get_user_model()

def path_and_rename(instance, filename):
    upload_to = 'posts'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Post(models.Model):
	 user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
	 created_at = models.DateTimeField(auto_now=True)
	 message = models.TextField()
	 message_html = models.TextField(editable=False)
	 image = models.ImageField(upload_to=path_and_rename, null=True,blank=True)
	 group = models.ForeignKey(Group,related_name='posts',null=True,blank=False,on_delete=models.CASCADE)

	 def __str__(self):
	 	return self.message

	 def save(self,*args,**kwargs):
		 self.message_html = misaka.html(self.message)
		 super().save(*args,**kwargs)

	 def get_absolute_url(self):
		 return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})
		#pk is for a primary key

	 class Meta:
		 ordering = ['-created_at']
