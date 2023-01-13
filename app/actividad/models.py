from django.db import models
# Create your models here.


class Tiposdoc(models.Model):
    status = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=5, blank=True, null=True)
    descrip = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposdoc'


class Clientes(models.Model):
    status = models.IntegerField()
    nombre = models.CharField(max_length=64)
    descrip = models.CharField(max_length=256, blank=True, null=True)
    direccion = models.CharField(max_length=32, blank=True, null=True)
    postal = models.ForeignKey('parametros.Postal', models.DO_NOTHING, blank=True, null=True)
    telefonos = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    establecim = models.CharField(max_length=64, blank=True, null=True)
    actividad = models.CharField(max_length=32, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    tipodoc = models.ForeignKey('Tiposdoc', models.DO_NOTHING, blank=True, null=True)
    documento = models.CharField(max_length=11, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    seg_retiro = models.IntegerField(blank=True, null=True)
    corresp = models.IntegerField(blank=True, null=True)
    reg_num = models.CharField(max_length=16, blank=True, null=True)
    reg_categ = models.CharField(max_length=16, blank=True, null=True)
    reg_juris = models.CharField(max_length=16, blank=True, null=True)
    reg_venc = models.DateField(blank=True, null=True)
    productor = models.ForeignKey('Productores', models.DO_NOTHING, blank=True, null=True)
    banco = models.CharField(max_length=32, blank=True, null=True)
    banco_suc = models.CharField(max_length=8, blank=True, null=True)
    banco_caja = models.CharField(max_length=16, blank=True, null=True)
    banco_ctacte = models.CharField(max_length=16, blank=True, null=True)
    debaut = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'clientes'
        ordering = ('nombre',)


class ClientesMediosdepago(models.Model):
    status = models.IntegerField()
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)
    mediodepago = models.ForeignKey('parametros.Mediosdepago', models.DO_NOTHING, blank=True, null=True)
    numero = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.numero

    class Meta:
        managed = False
        db_table = 'clientes_mediosdepago'


class Companias(models.Model):
    nombre = models.CharField(max_length=32)
    razon_social = models.CharField(max_length=64, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    direccion = models.CharField(max_length=32, blank=True, null=True)
    telefonos = models.CharField(max_length=32, blank=True, null=True)
    productor = models.ForeignKey('actividad.Productores', models.DO_NOTHING, blank=True, null=True)
    dias_primer_cuota = models.IntegerField(blank=True, null=True, verbose_name='Días a la primera cuota')
    liquidaciones = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name='Liquidaciones')
    prop_iva = models.BooleanField(default=True, verbose_name='Propor. IVA en la primera cuota')
    agente_iva = models.BooleanField(default=True, verbose_name='Agente retenc. IVA')
    comis_con_iva = models.BooleanField(default=True, verbose_name='Comisiones con IVA')
    ib_comis_prod = models.BooleanField(default=True, verbose_name='Productores')
    ib_comis_cobr = models.BooleanField(default=True, verbose_name='Cobradores')
    comis_cobranzas = models.IntegerField(blank=True, null=True)
    primer_cuota_iva = models.IntegerField(blank=True, null=True)
    fecha_firma_convenio = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'companias'
        ordering = ('nombre',)

class Monedas(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    simbolo = models.CharField(max_length=5, blank=True, null=True)
    cambio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monedas'

class Coberturas(models.Model):
    nombre = models.CharField(max_length=64, db_collation='latin1_swedish_ci')
    seccion = models.ForeignKey('Secciones', models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        managed = False
        db_table = 'coberturas'

class Mediosdepago(models.Model):
    nombre = models.CharField(max_length=64)
    tipo = models.CharField(max_length=16)
    status = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        managed = False
        db_table = 'mediosdepago'

class Tipospedido(models.Model):
    nombre = models.CharField(max_length=32, verbose_name='Tipo de Pedido')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tipospedido'
        ordering = ('nombre',)


class Tipospoliza(models.Model):
    nombre = models.CharField(max_length=32, verbose_name='Tipo de Póliza')
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tipospoliza'
        ordering = ('nombre',)


class Ordenes(models.Model):
    numero = models.IntegerField(blank=True, null=True, db_index=True)
    fecha = models.DateField(blank=True, null=True)
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True, db_index=True)
    productor = models.ForeignKey('Productores', models.DO_NOTHING, blank=True, null=True, db_index=True)
    # organizador = models.ForeignKey('Organizadores', models.DO_NOTHING, blank=True, null=True)
    moneda = models.ForeignKey(Monedas, models.DO_NOTHING, blank=True, null=True, db_index=True)
    compania = models.ForeignKey(Companias, models.DO_NOTHING, blank=True, null=True, db_index=True)
    seccion = models.ForeignKey('Secciones', models.DO_NOTHING, blank=True, null=True, db_index=True)
    cobertura = models.ForeignKey(Coberturas, models.DO_NOTHING, blank=True, null=True, db_index=True)
    tiposoli = models.ForeignKey('Tipospedido', models.DO_NOTHING, blank=True, null=True, db_index=True)
    suma = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    prima = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    recargos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    bonificacion = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    premio = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    tipopoliza = models.ForeignKey('Tipospoliza', models.DO_NOTHING, blank=True, null=True, db_index=True)
    riesgo_desc = models.TextField(blank=True, null=True)
    riesgo_valor = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    bien_asegurado = models.CharField(max_length=80, blank=True, null=True)
    produccion = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    cobranza = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    recup_gastos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    mediodepago = models.ForeignKey(Mediosdepago, models.DO_NOTHING, blank=True, null=True)
    nro_mediopago = models.CharField(max_length=32, blank=True, null=True)
    responsable = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=32, blank=True, null=True)
    # postal = models.ForeignKey('Postal', models.DO_NOTHING, blank=True, null=True)
    # poliza = models.ForeignKey('Polizas', models.DO_NOTHING, blank=True, null=True)
    num_poliza_ref = models.CharField(max_length=32, blank=True, null=True)
    cod_productor = models.CharField(max_length=16, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    codigo_productor = models.IntegerField(blank=True, null=True)
    orden_productor = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        managed = False
        db_table = 'ordenes'
        unique_together = (('numero', 'flag'),)

class Secciones(models.Model):
    nombre = models.CharField(max_length=32)
    descrip = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    abrev = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'secciones'
        ordering = ('nombre',)


class Productores(models.Model):
    nombre = models.CharField(max_length=32)
    status = models.IntegerField()
    direccion = models.CharField(max_length=64, blank=True, null=True)
    telefonos = models.CharField(max_length=64, blank=True, null=True)
    postal = models.ForeignKey('parametros.Postal', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    org1_id = models.IntegerField(blank=True, null=True)
    org2_id = models.IntegerField(blank=True, null=True)
    matricula = models.CharField(max_length=10, blank=True, null=True)
    ultima_orden = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'productores'
        ordering = ('nombre',)
