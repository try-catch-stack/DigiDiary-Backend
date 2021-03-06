# Generated by Django 4.0 on 2022-01-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_author'),
        ('authentication', '0004_alter_userprofile_bookmarked_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bookmarked_posts',
            field=models.ManyToManyField(blank=True, default=None, to='posts.Post'),
        ),
    ]
