# Generated by Django 4.0 on 2022-01-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_author'),
        ('authentication', '0003_remove_userprofile_email_remove_userprofile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bookmarked_posts',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Post'),
        ),
    ]