# Generated by Django 5.1.3 on 2024-12-06 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='monto2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporte',
            name='monto3',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporte',
            name='montototal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporte',
            name='usuario',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
    ]
