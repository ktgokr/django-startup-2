# Generated by Django 4.0.4 on 2022-04-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boot', '0002_rename_submit_time_inquiry_create_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='fullname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='phone_number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
