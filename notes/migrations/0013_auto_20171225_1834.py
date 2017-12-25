# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_auto_20171224_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
