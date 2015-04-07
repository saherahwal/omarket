# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_subscriptiontype_subscription_description'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
