from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =60)
    project_image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length =200)
    link = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    
class Profile(models.Model):
    profile_image = models.ImageField(upload_to = 'images/')
    user_bio = models.CharField(max_length =200)
    contact_info = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
