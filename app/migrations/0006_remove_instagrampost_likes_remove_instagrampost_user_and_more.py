# Generated by Django 4.0.4 on 2022-06-05 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_instagrampost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagrampost',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='instagrampost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='InstagramPost',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]