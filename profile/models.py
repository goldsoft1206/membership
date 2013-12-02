from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone


class Boat(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    length = models.IntegerField()
    beam = models.CharField(max_length=30)
    draft = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('boat_detail', kwargs={'pk': self.pk})


MEMBERSHIP_TYPE = (
    ('RS', 'RS'),
    ('RP', 'RP'),
    ('A', 'A'),
)

class MembershipType(models.Model):
    name = models.CharField(max_length=2, choices = MEMBERSHIP_TYPE)
    dues_rate = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mtype_detail', kwargs={'pk': self.pk})


class Membership(models.Model):
    membership_name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=40)
    zip = models.CharField(max_length=10)
    year_joined = models.IntegerField()
    membership_type = models.ForeignKey(MembershipType)
    last_payment_date = models.DateTimeField()
    posted_date = models.DateTimeField()
    active = models.BooleanField()
    receive_snail_mail = models.BooleanField()
    boats = models.ManyToManyField(Boat)

    def __unicode__(self):
        return self.membership_name

    def get_absolute_url(self):
        return reverse('membership_detail', kwargs={'pk': self.pk})


class EmailList(models.Model):
    list_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    list_owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse('email_detail', kwargs={'pk': self.pk})


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    membership = models.ForeignKey(Membership, blank=True, null=True)
    email_lists = models.ManyToManyField(EmailList, blank=True, null=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})

