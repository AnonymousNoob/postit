# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20171220_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='notehistory',
            name='title',
            field=models.CharField(max_length=100, default='Book Title'),
            preserve_default=False,
        ),
    ]
