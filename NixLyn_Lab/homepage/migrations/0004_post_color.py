# Generated by Django 4.2 on 2023-04-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_post_add_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='color',
            field=models.TextField(default='blue'),
        ),
    ]
