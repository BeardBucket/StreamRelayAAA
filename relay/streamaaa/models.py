import uuid

from django.db import models
from django.contrib.auth.models import User, Group

class StreamUser(models.Model):
    """ Extra fields off User model """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False,null=False)
    quick = models.SlugField(max_length=100, unique=True, editable=False,null=False)

class StreamGroup(models.Model):
    """ Extra fields off Group model """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,null=False)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, editable=False,null=False)
    quick = models.SlugField(max_length=100, unique=True, editable=False,null=False)


class StreamKey(models.Model):
    """ Stream keys """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,null=False)
    quick = models.SlugField(max_length=100, unique=True, editable=False,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,null=False)


class Relay(models.Model):
    """ A stream relay server """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,null=False)
    quick = models.SlugField(max_length=100, unique=True, editable=False,null=False)
    name = models.CharField(max_length=256)


class GroupRelayAccess(models.Model):
    """ Relay access to Group model """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,null=False)
    quick = models.SlugField(max_length=100, unique=True, editable=False,null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    relays_push = models.ManyToManyField(Relay, through='WithPush')
    relays_pull = models.ManyToManyField(Relay, through='WithPull')


