# Generated by Django 4.2 on 2023-05-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datum',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AddField(
            model_name='post',
            name='hely',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='tancos',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='tanctipus',
            field=models.TextField(default='', max_length=100),
        ),
    ]
