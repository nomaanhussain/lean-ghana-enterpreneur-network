# Generated by Django 2.2 on 2019-11-11 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0019_auto_20191111_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='category',
            new_name='categories',
        ),
    ]