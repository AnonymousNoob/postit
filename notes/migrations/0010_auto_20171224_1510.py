# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20171224_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notehistory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
