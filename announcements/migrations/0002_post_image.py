# Generated by Django 2.1.4 on 2018-12-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
