from django.db import models
from django.contrib.auth.models import User


class Boat(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    length = models.IntegerField()
    beam = models.CharField(max_length=30)
    draft = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


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


class EmailList(models.Model):
    list_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    list_owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.list_name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    membership = models.ForeignKey(Membership, blank=True, null=True)
    email_lists = models.ManyToManyField(EmailList, blank=True, null=True)

    def __unicode__(self):
        return self.user.email


