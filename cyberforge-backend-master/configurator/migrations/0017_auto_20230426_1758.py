# Generated by Django 3.2.18 on 2023-04-26 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0016_auto_20230426_0026'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Processor',
            new_name='CPU',
        ),
        migrations.RenameModel(
            old_name='GraphicsCard',
            new_name='GPU',
        ),
    ]
