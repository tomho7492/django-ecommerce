# Generated by Django 3.0.7 on 2020-06-07 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200607_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
