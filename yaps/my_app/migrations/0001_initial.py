# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('total_msg_counter', models.IntegerField(default=0)),
                ('success_msg_counter', models.IntegerField(default=0)),
                ('failed_msg_counter', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
