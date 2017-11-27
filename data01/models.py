from django.db import models
from django.utils import timezone
#import django_filters

# Create your models here.

class pd1_time(models.Model): #하루행사 시간
    title = models.CharField(max_length=20, default='default title')
    date = models.DateField(default='2000-01-01') #only date DateField
    starttime = models.TimeField(default='12:00') #only time TimeField
    endtime = models.TimeField(default='12:00')
    theme = models.TextField(default='default theme')
    who = models.CharField(max_length=20, default='default who')
    where = models.CharField(max_length=20, default='default where')

    def __str__(self):
        return self.title


class pd2(models.Model): #전체 정보
    kind = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    startdate = models.DateField(blank=True, null=True) #only date DateField
    enddate = models.DateField(blank=True, null=True)

    starttime = models.TimeField(blank=True, null=True) #only time TimeField
    endtime = models.TimeField(blank=True, null=True)

    theme = models.TextField(blank=True, null=True)
    who = models.CharField(max_length=20, blank=True, null=True)
    where = models.CharField(max_length=20, blank=True, null=True)

    addurl = models.URLField(max_length=100, blank=True, null=True)
    imgurl = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
