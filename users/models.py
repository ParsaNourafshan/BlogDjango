from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='Images')


    def __str__(self):

        return self.user.username

    def get_absolute_url(self):
        return reverse('post_detail', kwargs = {'pk': self.pk})