# Generated by Django 3.2.8 on 2021-10-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_details_tasks_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]