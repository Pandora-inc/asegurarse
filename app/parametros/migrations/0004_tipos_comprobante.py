# Generated by Django 4.1.3 on 2023-02-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0003_alter_banco_options_alter_bancosucu_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipos_comprobante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrip', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo de comprobante',
                'verbose_name_plural': 'Tipos de comprobante',
                'db_table': 'tipos_comprobantes',
            },
        ),
    ]
