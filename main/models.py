from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    name = models.CharField(max_length=123)
    icon = models.ImageField(upload_to='images/', null=True)
    image = models.FileField(upload_to='images/')
    description = models.TextField()
    text = RichTextField()
    text_2 = RichTextField(null=True, blank=True)
    text_3 = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class GoalAssessment(models.Model):
    title = models.CharField(max_length=333)
    icon = models.ImageField(upload_to='images/', null=True)
    content = RichTextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Certificate(models.Model):
    name = models.CharField(max_length=123)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=123)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name


class Numbers(models.Model):
    experience = models.CharField(max_length=123)
    works_done = models.IntegerField()
    clients = models.PositiveIntegerField()
    time_for_access = models.CharField(max_length=123)

    def __str__(self):
        return self.experience


class WhenNeedAssessment(models.Model):
    icon = models.FileField(upload_to='files/')
    title = models.CharField(max_length=1234)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=233)
    phone = models.CharField(max_length=23)

    def __str__(self):
        return self.name

