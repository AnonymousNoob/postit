# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_notehistory_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notehistory',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notehistory',
            name='note',
            field=models.ForeignKey(related_name='history', to='notes.Note', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notehistory',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notehistory',
            name='version',
            field=models.IntegerField(editable=False, null=True, blank=True),
        ),
    ]
