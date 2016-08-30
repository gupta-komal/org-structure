from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organisation(models.Model):
    """
    Organisation Details
    """
    name = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    """
     Team Details
    """
    name = models.CharField(max_length=512, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, related_name='user_team')
    org = models.ForeignKey(Organisation, null=True, blank=True, related_name='org_team')
    parent_team = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name


class Repo(models.Model):
    """
     Repo associated with Team
    """
    repo_name = models.CharField(max_length=512, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True, related_name='team_repo')

    def __str__(self):
        return self.repo_name