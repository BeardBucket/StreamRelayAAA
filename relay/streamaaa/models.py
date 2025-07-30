import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from .names import generate_name_f


class StreamUser(models.Model):
    """ Extra fields off User model """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, null=False)
    quick = models.SlugField(max_length=100, default=generate_name_f(num=5), unique=True, editable=False, null=False)
    handle = models.CharField(max_length=100, unique=True, null=False, editable=True, blank=False)

    def __str__(self):
        return f"{self.user.username} | {self.handle}"


class StreamGroup(models.Model):
    """ Extra fields off Group model """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, null=False)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, editable=False, null=False)
    quick = models.SlugField(max_length=100, default=generate_name_f(num=5), unique=True, editable=False, null=False)
    handle = models.CharField(max_length=100, unique=True, null=False, editable=True, blank=False)

    def __str__(self):
        return f"{self.group.name} | {self.handle}"


class StreamKey(models.Model):
    """ Stream keys """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, null=False)
    quick = models.SlugField(max_length=100, default=generate_name_f(num=5), unique=True, editable=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False)
    key = models.SlugField(max_length=128, default=generate_name_f(num=5), unique=True, editable=True, null=False)
    enabled = models.BooleanField(default=False, editable=True, null=False, blank=False)

    def __str__(self):
        return f"Key-{self.key}"


class Relay(models.Model):
    """ A stream relay server """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, null=False)
    quick = models.SlugField(max_length=100, default=generate_name_f(num=5), unique=True, editable=False, null=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"Relay-{self.name}"


class GroupRelayAccess(models.Model):
    """ Relay access to Group model """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, null=False)
    quick = models.SlugField(max_length=100, default=generate_name_f(num=5), unique=True, editable=False, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    relays_push = models.ManyToManyField(Relay, related_name='with_push')
    relays_pull = models.ManyToManyField(Relay, related_name='with_pull')

    def __str__(self):
        return f"RelayAccess-{self.group.name}"



