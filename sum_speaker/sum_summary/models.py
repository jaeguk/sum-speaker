from django.db import models
from datetime import datetime
from .naver_collections import show_top_issue

# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.TextField(max_length=50)
    password = models.CharField(max_length=50)
    reg_date = models.DateTimeField(default=datetime.now(), blank=True)
    update_date = models.DateTimeField(default=datetime.now(), blank=True)

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=20)
    link = models.TextField(max_length=255)
    title = models.TextField(max_length=255)
    author = models.TextField(max_length=20)
    summary = models.TextField()
    reg_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.keyword

class Images(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    reg_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Images

class Bookmark(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    keywords_id = models.TextField(max_length=255)
    keyword = models.CharField(max_length=255)
    status  = models.CharField(max_length=2)
    reg_date = models.DateTimeField(default=datetime.now(), blank=True)
    update_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.keyword