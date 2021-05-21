# Generated by Django 3.2 on 2021-05-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='firstname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(default=123456),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]