from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.utils.encoding import python_2_unicode_compatible # 파이썬2와 호환


class User(AbstractUser):
    # AbstractUser 에는 비번, 유저명, 이메일, 성 등이 디폴트로 존재
    # Instagram 에는 website, bio, phone, sex 없음

    """ User Models """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
