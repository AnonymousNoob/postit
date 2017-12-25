# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20171222_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 23, 12, 1, 59, 515381, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
