# Generated by Django 5.0.4 on 2024-07-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_calling',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
