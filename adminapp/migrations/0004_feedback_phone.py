# Generated by Django 5.0.7 on 2024-10-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='phone',
            field=models.CharField(default=910201, max_length=15),
            preserve_default=False,
        ),
    ]
