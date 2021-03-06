# Generated by Django 4.0 on 2021-12-31 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_userprofile_email_remove_userprofile_name_and_more'),
        ('posts', '0002_post_created_at_post_updated_at_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
    ]
