# Generated by Django 4.1.3 on 2023-02-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0013_alter_comprobantes_options_alter_cuotas_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuotas',
            old_name='rendicion_id',
            new_name='rendicion',
        ),
        migrations.RenameField(
            model_name='rendiciones',
            old_name='compania_id',
            new_name='compania',
        ),
        migrations.RenameField(
            model_name='rendiciones',
            old_name='productor_id',
            new_name='productor',
        ),
        migrations.RemoveField(
            model_name='cuotas',
            name='poliza_id',
        ),
        migrations.AddField(
            model_name='cuotas',
            name='poliza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='actividad.polizas', verbose_name='Poliza'),
        ),
        migrations.AlterModelTable(
            name='cuotas',
            table='cuotas_polizas',
        ),
    ]