from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    """ User Model """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified'),
    )

    profile_image = models.ImageField(blank=True, null=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=140, blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='user_followers')
    following = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='user_following')


    def __str__(self):
        return self.username

    @property
    def post_count(self):
        return self.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()
        