from django.db import models


# Create your models here.


class Banco(models.Model):
    descrip = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return str(self.descrip)

    class Meta:
        managed = False
        db_table = 'banco'
        ordering = ('descrip',)


class Bancosucu(models.Model):
    descrip = models.CharField(max_length=32, blank=True, null=True)
    codigo = models.CharField(max_length=16, blank=True, null=True)
    banco = models.ForeignKey(Banco, models.DO_NOTHING)

    def __str__(self):
        return str(self.descrip)

    class Meta:
        managed = False
        db_table = 'bancosucu'
        ordering = ('descrip',)


# Table with FK (Foreign Key)
class Provincias(models.Model):
    nombre = models.CharField(max_length=32)
    orden = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'provincias'


class Postal(models.Model):
    cp = models.CharField(max_length=4, verbose_name='CP')
    cpa = models.CharField(max_length=16, verbose_name='CPA')
    referencia = models.CharField(max_length=64,  verbose_name='Referencia')
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING, blank=True, null=True, verbose_name='Provincia')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.referencia)

    class Meta:
        managed = False
        db_table = 'postal'
        ordering = ('referencia',)


class Monedas(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    simbolo = models.CharField(max_length=5, blank=True, null=True)
    cambio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'monedas'

class Tipospedido(models.Model):
    nombre = models.CharField(max_length=32, verbose_name='Tipo de Pedido')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'tipospedido'
        ordering = ('nombre')


class Tipospoliza(models.Model):
    nombre = models.CharField(max_length=32, verbose_name='Tipo de Póliza')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'tipospoliza'
        ordering = ('nombre')



TIPOS_MEDIO_DE_PAGO = [
    ('Tarjeta', 'Tarjeta'),
    ('Cuenta', 'Cuenta'),
    ('Otro', 'Otro'),
    ]

class Mediosdepago(models.Model):
    nombre = models.CharField(max_length=64,verbose_name='Medio')
    tipo = models.CharField(max_length=16, choices=TIPOS_MEDIO_DE_PAGO, verbose_name='Tipo')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'mediosdepago'
        ordering = ('nombre',)

class Tiposdoc(models.Model):
    """ Clase con los tipos de documentos """

    nombre = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    status = models.IntegerField(blank=True, null=True)
    descrip = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'tiposdoc'
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'