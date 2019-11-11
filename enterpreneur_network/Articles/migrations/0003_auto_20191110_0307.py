# Generated by Django 2.2 on 2019-11-10 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articles', '0002_auto_20191109_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', help_text='Status of articles', max_length=1),
        ),
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='insta',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='linkedin',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='others',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
