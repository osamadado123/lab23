from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class heroes(models.Model):
    name=models.CharField(max_length=255)
    img_url=models.TextField(help_text='Pls enter an image url')
    attack_type=models.TextField(help_text='enter the hero attack type(melee, ranged)')
    roles=models.TextField(help_text='enter hero role/s')
    creator = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('heroes-detail', args=[self.id])