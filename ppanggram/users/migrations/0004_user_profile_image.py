# Generated by Django 2.0.9 on 2019-01-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181220_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]