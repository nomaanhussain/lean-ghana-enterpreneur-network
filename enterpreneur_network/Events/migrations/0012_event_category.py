# Generated by Django 2.2 on 2019-11-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_event_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='Events.Category'),
        ),
    ]
