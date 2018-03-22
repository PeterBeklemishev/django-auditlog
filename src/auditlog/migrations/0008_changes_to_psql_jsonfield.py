# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import migrations, models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

def copy_str_changes_to_json(apps, schema_editor):
    LogEntry = apps.get_model('auditlog','LogEntry')
    for entry in LogEntry.objects.raw('SELECT * FROM auditlog_logentry'):
        entry.changes = json.loads(entry.changes_old)
        entry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0007_object_pk_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logentry',
            old_name='changes',
            new_name='changes_old',
        ),
        migrations.AddField(
            model_name='logentry',
            name='changes',
            field=JSONField(null=True, verbose_name=_("change message")),
        ),
        migrations.RunPython(copy_str_changes_to_json),
        migrations.RemoveField(
            model_name='logentry',
            name='changes_old',
        ),
    ]
