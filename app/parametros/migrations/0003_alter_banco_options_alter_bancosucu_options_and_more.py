# Generated by Django 4.1.3 on 2023-02-09 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_alter_organizador_status_alter_provincias_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banco',
            options={'ordering': ('descrip',), 'verbose_name': 'banco', 'verbose_name_plural': 'bancos'},
        ),
        migrations.AlterModelOptions(
            name='bancosucu',
            options={'ordering': ('descrip',), 'verbose_name': 'sucursal', 'verbose_name_plural': 'sucursales'},
        ),
        migrations.AlterModelOptions(
            name='mediosdepago',
            options={'ordering': ('nombre',), 'verbose_name': 'medio de pago', 'verbose_name_plural': 'medios de pago'},
        ),
        migrations.AlterModelOptions(
            name='monedas',
            options={'verbose_name': 'moneda', 'verbose_name_plural': 'monedas'},
        ),
        migrations.AlterModelOptions(
            name='organizador',
            options={'verbose_name': 'organizador', 'verbose_name_plural': 'organizadores'},
        ),
        migrations.AlterModelOptions(
            name='postal',
            options={'ordering': ('referencia',), 'verbose_name': 'codigo postal', 'verbose_name_plural': 'codigos postales'},
        ),
        migrations.AlterModelOptions(
            name='provincias',
            options={'verbose_name': 'provincia', 'verbose_name_plural': 'provincias'},
        ),
        migrations.AlterModelOptions(
            name='tipospedido',
            options={'ordering': ('nombre', 'status'), 'verbose_name': 'tipo de pedido', 'verbose_name_plural': 'tipos de pedido'},
        ),
        migrations.AlterModelOptions(
            name='tipospoliza',
            options={'ordering': ('nombre', 'status'), 'verbose_name': 'tipo de poliza', 'verbose_name_plural': 'tipos de poliza'},
        ),
    ]
