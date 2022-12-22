from django.db import models
from django.utils import timezone
import datetime
from django.contrib import  admin

class URL(models.Model):
    URL = models.URLField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    text_data = models.TextField()

    def __str__(self):
        return self.URL
    

