# Generated by Django 4.0.4 on 2022-04-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inquiry',
            old_name='submit_time',
            new_name='create_at',
        ),
        migrations.AddField(
            model_name='inquiry',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]