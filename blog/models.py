from __future__ import unicode_literals

from django.db import models

# Create your models here.
class About_me(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField()
    pic_url = models.URLField()
    def __str__(self):
        return self.namema

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField()
    content = models.TextField()
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.name





