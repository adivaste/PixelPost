from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
      title = models.CharField(max_length=255, null=True)
      image = models.ImageField(upload_to="images/", null=False)
      description = models.TextField(blank=True, null=True)
      account = models.ForeignKey("Account", on_delete=models.CASCADE)

      def __str__(self):
            return str(self.title)

class Account(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
      avatar = models.ImageField(upload_to="avatar/")
      
      def __str__(self):
            return str(self.user.username)
