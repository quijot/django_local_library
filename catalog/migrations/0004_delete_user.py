# Generated by Django 3.0.5 on 2020-05-02 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200502_1752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]