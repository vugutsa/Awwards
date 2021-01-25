from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Projects(models.Model):
    project_title = models.CharField(max_length =60)
    project_image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length =200)
    link = models.URLField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def save_projects(self):
        self.save()
    
    def delete_projects(self):
        self.delete()
           
    @classmethod
    def search_by_project_title(cls,search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
     
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def get_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects
    @classmethod
    def get_projects(request, id):
        try:
            project = Projects.objects.get(pk = id)
        except ObjectDoesNotExist:
            raise Http404()
        return projects
            
    def __str__(self):
        return self.description

    
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
        return self.user_bio
    
class AwardsMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    bio = models.DecimalField(decimal_places=2, max_digits=20) 
    profile_image = models.ImageField(upload_to = 'images/')
    link = models.URLField()
    