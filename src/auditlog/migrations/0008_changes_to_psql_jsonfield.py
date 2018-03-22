# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import migrations, models
from auditlog.models import logentry
from django.contrib.postgres.fields import JSONField

def copy_str_changes_to_json(apps, schema_editor):
    AuthorPublisherProfile = apps.get_model('portal','AuthorPublisherProfile')
    for entry in logentry.objects.all():
        entry.changes_json = json.loads(entry.changes)
        entry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0007_object_pk_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='changes_json',
            field=JSONField(null=True, verbose_name=_("change message")),
        ),
        migrations.RunPython(copy_str_changes_to_json),
        migrations.RemoveField(
            model_name='logentry',
            name='changes',
        ),
        migrations.RenameField(
            model_name='logentry',
            old_name='changes_json',
            new_name='changes',
        ),
    ]
