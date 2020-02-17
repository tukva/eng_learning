from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import Choices
from multiselectfield import MultiSelectField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Teacher(models.Model):
    LANGUAGES = Choices(
        ('ENGLISH', 'English'),
        ('SPANISH', 'Spanish'),
        ('FRENCH', 'French'),
        ('GERMANY', 'Germany'), )

    LEVEL_OF_LANGUAGE = Choices(
        ('BEGINNER', 'Beginner'),
        ('ELEMENTARY', 'Elementary'),
        ('PRE_INTERMEDIATE', 'Pre-Intermediate'),
        ('INTERMEDIATE', 'Intermediate'),
        ('UPPER_INTERMEDIATE', 'Upper-Intermediate'),
        ('ADVANCE', 'Advance'), )

    DAYS_OF_WEEK = Choices(
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'), )

    TYPES_OF_LESSON = Choices(
        ('ZNO', 'Zno'),
        ('SPEAKING', 'Speaking'),
        ('BUSINESS', 'Business'),
        ('TRAVELING', 'Traveling'), )

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGES, max_length=12, default=LANGUAGES.ENGLISH)
    own_level_of_language = models.CharField(choices=LEVEL_OF_LANGUAGE, max_length=20)
    level_of_training = MultiSelectField(choices=LEVEL_OF_LANGUAGE)
    days_of_work = MultiSelectField(choices=DAYS_OF_WEEK)
    types_of_lesson = MultiSelectField(choices=TYPES_OF_LESSON)

    def __str__(self):
        return f'{self.profile.user.username}'


class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username}'
