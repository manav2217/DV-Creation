# Generated by Django 3.2 on 2021-05-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210515_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
