# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('user', models.OneToOneField(related_name='msg', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('total_msg_counter', models.IntegerField(default=0)),
                ('success_msg_counter', models.IntegerField(default=0)),
                ('failed_msg_counter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Messages',
                'verbose_name_plural': 'Message',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ava', models.CharField(max_length=b'30')),
                ('token', models.CharField(max_length=b'30')),
                ('user', models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profiles',
                'verbose_name_plural': 'Profile',
            },
            bases=(models.Model,),
        ),
    ]
