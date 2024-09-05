from django.db import models

from django.contrib.auth.models import AbstractUser


class Custom_user(AbstractUser):
    
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker')
    ]
    
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Age=models.PositiveIntegerField(null=True)
    Contact_No=models.CharField(max_length=100,null=True)
    
    def __str__(self):  
        
        return f"{self.first_name}-{self.last_name}-{self.username}-{self.Age}"
    
    
    
    
    
    