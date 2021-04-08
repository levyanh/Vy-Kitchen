# Generated by Django 3.2 on 2021-04-08 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210407_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avarta',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_avatar.jpg', upload_to='user_avatar'),
        ),
    ]