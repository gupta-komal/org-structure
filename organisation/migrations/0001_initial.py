# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('repo_name', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('org', models.ForeignKey(related_name='org_team', to='organisation.Organisation', blank=True, null=True)),
                ('parent_team', models.ForeignKey(to='organisation.Team', blank=True, null=True)),
                ('user', models.ForeignKey(related_name='user_team', to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='repo',
            name='team',
            field=models.ForeignKey(related_name='team_repo', to='organisation.Team', blank=True, null=True),
        ),
    ]
