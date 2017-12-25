# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_note_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='notehistory',
            options={'ordering': ['-version']},
        ),
    ]
