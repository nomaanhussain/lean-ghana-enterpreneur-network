# Generated by Django 2.2 on 2019-11-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0009_event_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=True, verbose_name='Event Description'),
            preserve_default=False,
        ),
    ]
