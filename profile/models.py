from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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
    list_owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse('email_detail', kwargs={'pk': self.pk})


class UserProfile(models.Model):
    birth_date = models.DateField()
    phone = models.CharField(max_length=30)
    membership = models.ForeignKey(Membership)
    email_lists = models.ManyToManyField(EmailList)


