from django.db import models

class Lesson(models.Model):
    Shekh = models.CharField(max_length=200)
    Topic = models.CharField(max_length=200, default='')
    Description = models.CharField(max_length=300, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='audio_files/', null=True, blank=True)
    Book = models.FileField(upload_to='downloadable_files/', null=True, blank=True)

    def __str__(self):
        return self.Shekh

    

class Newz(models.Model):
    Events=models.CharField(max_length=200)
    Shekh=models.CharField(max_length=200)
    Location=models.CharField(max_length=200)
    Time=models.CharField(max_length=20 ,default='')
    def __str__(self):
        return self.Shekh
    
class Qur(models.Model):
    audio = models.FileField(upload_to='audio_files/', null=True, blank=True)
    msomaji = models.CharField(max_length=200)
    sura = models.CharField(max_length=200, default='')
   
