# Generated by Django 2.2 on 2019-11-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_auto_20191110_0338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
    ]
