from django.test import TestCase
from .models import Projects,Profile
import datetime as dt
# Create your tests here.

class ProjectsTestClass(TestCase):
    
    def setUp(self):
        # Creating a new profile and saving it
        self.projects = Projects()
        self.projects.save_projects()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_projects,Projects))
        
    def test_save_method(self):
        self.new_iprojects.save_projects()
        new_projects = Projects.objects.all()      
        self.assertTrue(len(new_projects) >0)
        
    def test_delete_projects(self):
        self.new_projects.delete_projects()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)== 0)

     
class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.profile = Profile()
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    # Testing Save Method
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)== 0) 
        
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.id, 'Mombasa')
        changed_profile = profile.objects.filter(name ='Mombasa')
        self.assertTrue(len(changed_profile) > 0)   
        
    def tearDown(self):
        Projects.objects.all().delete()
        Profile.objects.all().delete()   
                       