# Generated by Django 3.2.18 on 2023-04-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='custom_pcs',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='total_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='adjustable_speed',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='air_flow',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='connector',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='cooler_height',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='fan_diameter',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='maximum_rotation_speed',
        ),
        migrations.RemoveField(
            model_name='cooling',
            name='maximum_tdp',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='interface_transfer_rate',
        ),
        migrations.RemoveField(
            model_name='modification',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='modification',
            name='sound_card',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='num_pci_express_slots_x1',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='num_pci_express_slots_x16',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='integrated_graphics_system',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='l3_cache_size',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='microarchitecture',
        ),
        migrations.RemoveField(
            model_name='ram',
            name='supply_voltage',
        ),
        migrations.RemoveField(
            model_name='ram',
            name='timings',
        ),
        migrations.AddField(
            model_name='cooling',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cooling',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='graphicscard',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphicscard',
            name='rated_power',
            field=models.PositiveIntegerField(default=None, help_text='in W'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='housing',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='form_factor',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='modification',
            name='description',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modification',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powersupplyunit',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processor',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processor',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='processor',
            name='total_number_of_threads',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='graphicscard',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='housing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='powersupplyunit',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='CustomPC',
        ),
        migrations.DeleteModel(
            name='SoundCard',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
