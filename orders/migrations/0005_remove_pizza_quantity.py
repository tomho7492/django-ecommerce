# Generated by Django 3.0.7 on 2020-06-07 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200606_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='quantity',
        ),
    ]