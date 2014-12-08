# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ava',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(related_name='prof', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
