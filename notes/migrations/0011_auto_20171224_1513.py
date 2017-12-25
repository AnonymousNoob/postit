# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20171224_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notehistory',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
