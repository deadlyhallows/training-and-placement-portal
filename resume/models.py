from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Resume(models.Model):
    StudentName = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    ProjectsandInternships= models.CharField(max_length=200)
    StudentId=models.IntegerField()
    Branch=models.CharField(max_length=200)
    PhoneNumber=models.IntegerField()
    Cgpa = models.FloatField()
    TenthMarks=models.FloatField()
    TenthSchoolName = models.CharField(max_length=200)
    TwelthMarks=models.FloatField()
    TwelthCollegeName = models.CharField(max_length=200)

    def ResumeSave(self):
        self.save()







class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


