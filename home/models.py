# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projects(models.Model):

    #__Projects_FIELDS__
    project name = models.TextField(max_length=255, null=True, blank=True)
    customer name = models.TextField(max_length=255, null=True, blank=True)
    customer email = models.TextField(max_length=255, null=True, blank=True)
    project type = models.TextField(max_length=255, null=True, blank=True)
    budget = models.CharField(max_length=255, null=True, blank=True)
    customer nr = models.ForeignKey(Customers, on_delete=models.CASCADE)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class Hours(models.Model):

    #__Hours_FIELDS__
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    hours = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    rate = models.CharField(max_length=255, null=True, blank=True)
    worktype = models.TextField(max_length=255, null=True, blank=True)

    #__Hours_FIELDS__END

    class Meta:
        verbose_name        = _("Hours")
        verbose_name_plural = _("Hours")


class Customers(models.Model):

    #__Customers_FIELDS__
    customer number = models.CharField(max_length=255, null=True, blank=True)
    customer name = models.TextField(max_length=255, null=True, blank=True)
    customer email = models.CharField(max_length=255, null=True, blank=True)
    customer domain = models.CharField(max_length=255, null=True, blank=True)

    #__Customers_FIELDS__END

    class Meta:
        verbose_name        = _("Customers")
        verbose_name_plural = _("Customers")


class Darkweb Monitoring(models.Model):

    #__Darkweb Monitoring_FIELDS__
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    domain(s) = models.TextField(max_length=255, null=True, blank=True)

    #__Darkweb Monitoring_FIELDS__END

    class Meta:
        verbose_name        = _("Darkweb Monitoring")
        verbose_name_plural = _("Darkweb Monitoring")



#__MODELS__END
