# Generated by Django 5.0.6 on 2024-05-29 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfile',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='project.project'),
            preserve_default=False,
        ),
    ]
