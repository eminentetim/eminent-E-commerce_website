# Generated by Django 5.0.4 on 2024-04-04 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
