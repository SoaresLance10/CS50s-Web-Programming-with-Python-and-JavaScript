from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
	owner = models.CharField(max_length=64)
	title = models.CharField(max_length=64)
	description = models.TextField()
	category = models.CharField(max_length=64)
	price = models.IntegerField()
	pic = models.CharField(max_length=64, default=None, blank=True, null=True)
	time = models.CharField(max_length=64)

class Bid(models.Model):
	listing_id = models.IntegerField()
	title = models.CharField(max_length=64)
	user = models.CharField(max_length=64)
	bid = models.IntegerField()

class Comment(models.Model):
	listing_id = models.IntegerField()
	user = models.CharField(max_length=64)
	comment = models.TextField()
	time = models.CharField(max_length=64)

class Watchlist(models.Model):
	user = models.CharField(max_length=64)
	listing_id = models.IntegerField()

class Closedbid(models.Model):
	listing_id = models.CharField(max_length=64)
	owner = models.CharField(max_length=64)
	winner = models.CharField(max_length=64)
	price = models.IntegerField()
	
class All_listing(models.Model):
    listing_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    pic = models.CharField(max_length=64,default=None,blank=True,null=True)
