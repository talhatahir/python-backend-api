# Generated by Django 2.0.7 on 2018-07-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='listings',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(max_length=50),
        ),
    ]