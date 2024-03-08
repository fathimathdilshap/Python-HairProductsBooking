from django.db import models

# Create your models here.
class Category(models.Model):
    Title=models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title
    

class Post(models.Model):
    title=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=200)
    Description=models.TextField()
    Description2=models.TextField()
    Description3=models.TextField(default=0)
    image=models.ImageField(upload_to="static/image")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title