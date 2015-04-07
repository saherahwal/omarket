# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_auto_20141225_2212'),
        ('registration', '0003_auto_20141225_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='addresses',
            field=models.ManyToManyField(to='address.Address'),
            preserve_default=True,
        ),
    ]
