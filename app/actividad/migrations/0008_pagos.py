# Generated by Django 4.1.3 on 2023-02-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0007_cuotas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('importe', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tipo', models.CharField(max_length=2)),
                ('cuota_id', models.IntegerField()),
                ('comprobante_id', models.IntegerField()),
            ],
            options={
                'db_table': 'pagos_cuotas',
            },
        ),
    ]
