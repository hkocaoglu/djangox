from django.db import models
from django.urls import reverse
# from django.utils import date

# Create your models here.
class Equipment(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100)
    type  = models.CharField(max_length = 100)
    brand = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name = ("Equipment")
        verbose_name_plural = ("Equipments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Equipment_detail", kwargs={"pk": self.pk})

class Area(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100)
    dateCreate = models.DateField( auto_now=True)
    dateUpdate = models.DateField( auto_now=True)
 
    class Meta:
        verbose_name = ("Area")
        verbose_name_plural = ("Areas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Area_detail", kwargs={"pk": self.pk})

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100)
    area = models.ForeignKey('Area',on_delete=models.CASCADE,null=True)
    dateCreate = models.DateField( auto_now=True)
    dateUpdate = models.DateField( auto_now=True)
 
    class Meta:
        verbose_name = ("Location")
        verbose_name_plural = ("Locations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})



class Work(models.Model):

    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100)
    detail  = models.TextField(max_length = 2000, default="")
    dateCreate = models.DateField( auto_now_add=True)
    dateUpdate = models.DateField( auto_now=True)
    todo_later = models.BooleanField(default=False)
    stoppage = models.BooleanField(default=False)
    stopage_duration = models.FloatField(default=0)
    area  = models.ForeignKey('Area',on_delete=models.CASCADE,null=True)
    location  = models.ForeignKey('Location',on_delete=models.CASCADE,null=True)
    equipment = models.ForeignKey('Equipment', on_delete = models.CASCADE,null=True)
    class Meta:
        verbose_name = ("Work")
        verbose_name_plural = ("Works")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("work_detail", kwargs={"pk": self.pk})

