# Generated by Django 3.2 on 2022-08-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0002_auto_20220802_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
