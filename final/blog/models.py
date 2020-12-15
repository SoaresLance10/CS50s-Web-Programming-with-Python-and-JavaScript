from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Poster(models.Model):
	name = models.CharField(max_length=64)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=64, null=True)
	ttype = models.CharField(max_length=64, null=True)
	description = models.TextField(null=True)

class Posts(models.Model):
	poster = models.CharField(max_length=64)
	title = models.CharField(max_length=64)
	place = models.CharField(max_length=64)
	content = models.TextField()
	continent = models.CharField(max_length=64)
	timestamp = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField()

class Followinfo(models.Model):
    name = models.CharField(max_length=64)
    follower = models.CharField(max_length=64)

class Comment(models.Model):
	post_id = models.IntegerField()
	user = models.CharField(max_length=64)
	comment = models.TextField()
	time = models.CharField(max_length=64)

class Like(models.Model):
    post_id = models.IntegerField()
    likedby = models.CharField(max_length=64)
    likes = models.IntegerField()

class All_listing(models.Model):
	post_id = models.IntegerField()
	title = models.CharField(max_length=64)
	place = models.CharField(max_length=64)
	continent = models.CharField(max_length=64)

