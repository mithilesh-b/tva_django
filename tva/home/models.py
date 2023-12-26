from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    desc= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name
    

#for admin upload course

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    youtube_link = models.URLField()

    def __str__(self):
        return self.title

class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='materials/')

    def __str__(self):
        return self.title

