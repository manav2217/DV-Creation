# Generated by Django 3.2 on 2021-05-19 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20210519_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='user_email',
        ),
    ]
