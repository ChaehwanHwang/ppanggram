# Generated by Django 2.0.9 on 2019-02-05 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_notification_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
