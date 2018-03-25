from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Resume(models.Model):
    Name = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    ProjectsandInternships= models.TextField()
    PhoneNumber=models.IntegerField()
    Cgpa = models.FloatField()
    TenthMarks=models.FloatField()
    TenthCollegeName = models.CharField(max_length=200)
    TwelthMarks=models.FloatField()
    TwelthCollegeName = models.CharField(max_length=200)

    def ResumeSave(self):
        self.save()

    def __str__(self):
        return self.Name





class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


