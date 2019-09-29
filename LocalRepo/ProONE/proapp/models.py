from django.db import models


class ProData(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    email = models.EmailField(max_length=50)
    uname = models.CharField(max_length=20,primary_key=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class StoryData(models.Model):
    date = models.DateField(max_length=100)
    story = models.CharField(max_length=1200)

    def __str__(self):
        return self.date
