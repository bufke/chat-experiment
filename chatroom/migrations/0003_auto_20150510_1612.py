# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_room_add_by_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='organization',
            field=models.ManyToManyField(blank=True, to='chatroom.Organization'),
        ),
    ]
