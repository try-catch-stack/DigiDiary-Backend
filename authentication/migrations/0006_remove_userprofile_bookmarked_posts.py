# Generated by Django 4.0 on 2022-01-01 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_userprofile_bookmarked_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bookmarked_posts',
        ),
    ]
