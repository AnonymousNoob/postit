# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20171224_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notehistory',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='notehistory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 24, 9, 5, 49, 987881, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
