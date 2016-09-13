from django.db import models
from django.contrib.auth.models import User
#from datetime import date

class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=150)
    #fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
