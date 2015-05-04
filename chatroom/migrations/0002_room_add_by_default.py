# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='add_by_default',
            field=models.BooleanField(help_text='Organization users will automatically join this room.', default=True),
            preserve_default=True,
        ),
    ]
