# Generated by Django 3.0.7 on 2020-06-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200606_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]
