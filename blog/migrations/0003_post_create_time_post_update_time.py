# Generated by Django 4.0.1 on 2022-02-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
