from django.db import models


# Create your models here.


class Banco(models.Model):
    descrip = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return str(self.descrip)

    class Meta:
        # managed = False
        db_table = 'banco'
        verbose_name = 'banco'
        verbose_name_plural = 'bancos'
        ordering = ('descrip',)


class Bancosucu(models.Model):
    descrip = models.CharField(max_length=32, blank=True, null=True)
    codigo = models.CharField(max_length=16, blank=True, null=True)
    banco = models.ForeignKey(Banco, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.descrip)

    class Meta:
        # managed = False
        db_table = 'bancosucu'
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'
        ordering = ('descrip',)


# Table with FK (Foreign Key)
class Provincias(models.Model):
    nombre = models.CharField(max_length=32)
    orden = models.IntegerField()
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'
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
        # managed = False
        db_table = 'postal'
        verbose_name = 'codigo postal'
        verbose_name_plural = 'codigos postales'
        ordering = ('referencia',)


class Monedas(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    simbolo = models.CharField(max_length=5, blank=True, null=True)
    cambio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        verbose_name = 'moneda'
        verbose_name_plural = 'monedas'
        db_table = 'monedas'

class Tipospedido(models.Model):
    nombre = models.CharField(max_length=32, verbose_name='Tipo de Pedido')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        db_table = 'tipospedido'
        verbose_name = 'tipo de pedido'
        verbose_name_plural = 'tipos de pedido'
        ordering = ('nombre', 'status')


class Tipospoliza(models.Model):
    nombre = models.CharField(max_length=32, verbose_name='Tipo de Póliza')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        db_table = 'tipospoliza'
        verbose_name = 'tipo de poliza'
        verbose_name_plural = 'tipos de poliza'
        ordering = ('nombre', 'status')



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
        # managed = False
        db_table = 'mediosdepago'
        verbose_name = 'medio de pago'
        verbose_name_plural = 'medios de pago'
        ordering = ('nombre',)

class Tiposdoc(models.Model):
    """ Clase con los tipos de documentos """

    nombre = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    status = models.BooleanField(default=True, verbose_name='Activo')
    descrip = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'tiposdoc'
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'


class Organizador(models.Model):
    status = models.BooleanField(default=True, verbose_name='Activo')
    nombre = models.CharField(max_length=32)
    direccion = models.CharField(max_length=64)
    telefonos = models.CharField(max_length=64)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'organizadores'
        verbose_name = 'organizador'
        verbose_name_plural = 'organizadores'