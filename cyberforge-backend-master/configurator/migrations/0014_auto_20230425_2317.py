# Generated by Django 3.2.18 on 2023-04-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0013_auto_20230425_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphicscard',
            name='interface',
            field=models.CharField(choices=[('PCIe 3.0', 'PCIe 3.0'), ('PCIe 4.0', 'PCIe 4.0'), ('AGP', 'AGP')], default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphicscard',
            name='technical_process',
            field=models.PositiveIntegerField(default=8, help_text='in nm'),
        ),
        migrations.AlterField(
            model_name='graphicscard',
            name='chipset_model',
            field=models.CharField(choices=[('GTX1050Ti', 'GTX1050Ti'), ('GTX1060', 'GTX1060'), ('GTX1070', 'GTX1070'), ('GTX1080', 'GTX1080'), ('RTX2060', 'RTX2060'), ('RTX2070', 'RTX2070'), ('RTX2080', 'RTX2080'), ('RTX3060', 'RTX3060'), ('RTX3070', 'RTX3070'), ('RTX3080', 'RTX3080'), ('RTX4070', 'RTX4070')], max_length=10),
        ),
        migrations.AlterField(
            model_name='graphicscard',
            name='video_memory_type',
            field=models.CharField(choices=[('GDDR5', 'GDDR5'), ('GDDR5X', 'GDDR5X'), ('GDDR6', 'GDDR6'), ('GDDR6X', 'GDDR6X')], max_length=6),
        ),
    ]
