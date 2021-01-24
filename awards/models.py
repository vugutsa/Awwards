from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =60)
    project_image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length =200)
    link = models.URLField()
    
    
    
    def save_projects(self):
        self.save()
    
    def delete_projects(self):
        self.delete()
           
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects
     
               
    def __str__(self):
        return self.title

    
class Profile(models.Model):
    name = models.CharField(max_length =60)
    profile_image = models.ImageField(upload_to = 'images/')
    user_bio = models.CharField(max_length =200)
    contact_info = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_by_name(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return photo
    def __str__(self):
        return self.name