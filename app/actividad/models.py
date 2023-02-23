""" Modelo de datos relacionados a la actividad """
from django.db import models
from parametros.models import Banco, Bancosucu, Mediosdepago, Tiposdoc, Postal, Monedas, Tipospoliza, Tipospedido, Provincias, Organizador, Tipos_comprobante



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
        return str(self.nombre)

    class Meta:
        # managed = False
        db_table = 'companias'
        verbose_name = 'compania'
        verbose_name_plural = 'companias'
        ordering = ('nombre',)


class Productores(models.Model):
    nombre = models.CharField(max_length=32)
    matricula = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=64, blank=True, null=True)
    postal = models.ForeignKey('parametros.Postal', models.DO_NOTHING, blank=True, null=True)
    telefonos = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    org1_id = models.IntegerField(blank=True, null=True)
    org2_id = models.IntegerField(blank=True, null=True)
    ultima_orden = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')
    # companias = models.ManyToManyField(Companias)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        db_table = 'productores'
        verbose_name = 'productor'
        verbose_name_plural = 'productores'
        ordering = ('nombre',)

class Clientes(models.Model):
    # status = models.BooleanField(default=True)
    activo = models.BooleanField(default=True, blank=True, null=True)
    nombre = models.CharField(max_length=64)
    descrip = models.CharField(max_length=256, blank=True, null=True)
    direccion = models.CharField(max_length=64, blank=True, null=True)
    postal = models.ForeignKey(Postal, models.DO_NOTHING, blank=True, null=True)
    telefonos = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    establecim = models.CharField(max_length=64, blank=True, null=True)
    actividad = models.CharField(max_length=32, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    tipodoc = models.ForeignKey(Tiposdoc, models.DO_NOTHING, blank=True, null=True)
    documento = models.CharField(max_length=11, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    seg_retiro = models.BooleanField(blank=True, null=True)
    corresp = models.BooleanField(blank=True, null=True)
    reg_num = models.CharField(max_length=16, blank=True, null=True)
    reg_categ = models.CharField(max_length=16, blank=True, null=True)
    reg_juris = models.CharField(max_length=16, blank=True, null=True)
    reg_venc = models.DateField(blank=True, null=True)
    productor = models.ForeignKey(Productores, models.DO_NOTHING, blank=True, null=True)
    banco = models.CharField(max_length=32, blank=True, null=True)
    banco_suc = models.CharField(max_length=8, blank=True, null=True)
    banco_caja = models.CharField(max_length=16, blank=True, null=True)
    banco_ctacte = models.CharField(max_length=16, blank=True, null=True)
    debaut = models.BooleanField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    zona_cza = models.CharField(max_length=32, blank=True, null=True)
    fuente = models.CharField(max_length=32, blank=True, null=True)
    # ordenes = models.ManyToManyField('Ordenes', blank=True, null=True)
    # polizas = models.ManyToManyField('Polizas', blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'clientes'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ('nombre',)


class ClientesMediosdepago(models.Model):
    status = models.BooleanField(default=True, verbose_name='Activo')
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)
    mediodepago = models.ForeignKey(Mediosdepago, models.DO_NOTHING, blank=True, null=True)
    numero = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return str(self.numero)

    class Meta:
        # managed = False
        db_table = 'clientes_mediosdepago'


class Secciones(models.Model):
    nombre = models.CharField(max_length=32)
    descrip = models.CharField(max_length=64, blank=True, null=True)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        db_table = 'secciones'
        verbose_name = 'seccion'
        verbose_name_plural = 'secciones'
        ordering = ('nombre',)

class Coberturas(models.Model):
    nombre = models.CharField(max_length=64)
    seccion = models.ForeignKey('Secciones', models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        # managed = False
        verbose_name = 'cobertura'
        verbose_name_plural = 'coberturas'
        db_table = 'coberturas'


class Ordenes(models.Model):
    numero = models.IntegerField(blank=True, null=True, db_index=True)
    fecha = models.DateField(blank=True, null=True)
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True, db_index=True)
    productor = models.ForeignKey(Productores, models.DO_NOTHING, blank=True, null=True, db_index=True)
    organizador = models.ForeignKey(Organizador, models.DO_NOTHING, blank=True, null=True)
    moneda = models.ForeignKey(Monedas, models.DO_NOTHING, blank=True, null=True, db_index=True)
    compania = models.ForeignKey(Companias, models.DO_NOTHING, blank=True, null=True, db_index=True)
    seccion = models.ForeignKey(Secciones, models.DO_NOTHING, blank=True, null=True, db_index=True)
    cobertura = models.ForeignKey(Coberturas, models.DO_NOTHING, blank=True, null=True, db_index=True)
    # tiposol_id = models.ForeignKey(Tipospedido, models.DO_NOTHING, blank=True, null=True, db_index=True)
    suma = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    prima = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    recargos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    bonificacion = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    premio = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    tipopoliza = models.ForeignKey(Tipospoliza, models.DO_NOTHING, blank=True, null=True)
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
    postal = models.ForeignKey(Postal , models.DO_NOTHING, blank=True, null=True)
    localidad = models.CharField(max_length=32, blank=True, null=True)
    poliza = models.ForeignKey('Polizas', models.DO_NOTHING, blank=True, null=True)
    num_poliza_ref = models.CharField(max_length=32, blank=True, null=True)
    cod_productor = models.CharField(max_length=16, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    codigo_productor = models.IntegerField(blank=True, null=True)
    orden_productor = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return str(self.numero) # + " - " + str(self.productor)

    class Meta:
        # managed = False
        db_table = 'ordenes'
        verbose_name = 'orden'
        verbose_name_plural = 'ordenes'
        unique_together = (('numero', 'flag'),)





class Polizas(models.Model):
    # Orden
    # orden_id = models.IntegerField()
    numero = models.CharField(max_length=64)
    cliente = models.ForeignKey(Clientes, models.RESTRICT)
    productor = models.ForeignKey(Productores, models.RESTRICT)
    organizador = models.ForeignKey(Organizador, models.RESTRICT, blank=True, null=True)
    #Vigencia
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    # Riesgo
    direccion = models.CharField(max_length=64, null=True)
    postal = models.ForeignKey(Postal, models.RESTRICT)
    provincia = models.ForeignKey(Provincias, models.RESTRICT)
    # Poliza
    num_poliza = models.CharField(max_length=64, null=True)
    fecha = models.DateField(blank=True, null=True)
    tipopoliza = models.ForeignKey(Tipospoliza, models.RESTRICT, blank=True, null=True)
    seccion = models.ForeignKey(Secciones, models.RESTRICT)
    cobertura = models.ForeignKey(Coberturas, models.RESTRICT)
    compania = models.ForeignKey(Companias, models.RESTRICT)
    moneda = models.ForeignKey(Monedas, models.RESTRICT)
    # Siniestros
    siniestro01 = models.CharField(max_length=100, blank=True, null=True)
    siniestro02 = models.CharField(max_length=100, blank=True, null=True)
    siniestro03 = models.CharField(max_length=100, blank=True, null=True)
    siniestro04 = models.CharField(max_length=100, blank=True, null=True)
    # valores
    suma = models.DecimalField(max_digits=11, decimal_places=2)
    prima = models.DecimalField(max_digits=11, decimal_places=2)
    recargos = models.DecimalField(max_digits=11, decimal_places=2)
    bonificacion = models.DecimalField(max_digits=11, decimal_places=2)
    premio = models.DecimalField(max_digits=11, decimal_places=2)
    # Comisiones
    produccion = models.DecimalField(max_digits=11, decimal_places=2)
    cobranza = models.DecimalField(max_digits=11, decimal_places=2)
    recup_gastos = models.DecimalField(max_digits=11, decimal_places=2)
    # ???
    fecha_recepcion = models.DateField(blank=True, null=True)
    iva = models.DecimalField(max_digits=11, decimal_places=2)
    ing_brutos = models.DecimalField(max_digits=11, decimal_places=2)
    # Formas de pago
    mediodepago = models.ForeignKey(Mediosdepago, models.RESTRICT)
    nro_mediopago = models.CharField(max_length=64, null=True)
    cant_cuotas = models.IntegerField()

    bien_asegurado = models.CharField(max_length=80, null=True)
    riesgo_desc = models.TextField()
    status = models.BooleanField(default=True, verbose_name='Activo')

    riesgo_valor = models.DecimalField(max_digits=11, decimal_places=2,blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    nota_credito = models.BooleanField()
    telefonos = models.CharField(max_length=64, blank=True, null=True)
    restante = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.numero)

    class Meta:
        db_table = 'polizas'
        verbose_name = 'poliza'
        verbose_name_plural = 'polizas' 

class Rendiciones(models.Model):
    status = models.BooleanField(default=True, verbose_name='Activo')
    fecha = models.DateField(blank=True, null=True)
    productor = models.ForeignKey(Productores, models.RESTRICT, blank=True, null=True, verbose_name='Productor')
    fecha_cierre = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    compania = models.ForeignKey(Companias, models.RESTRICT, blank=True, null=True, verbose_name='Compañía')

    class Meta:
        db_table = 'rendiciones'
        verbose_name = 'Rendicion'
        verbose_name_plural = 'Rendiciones' 

class Comprobantes (models.Model):
    cliente = models.ForeignKey(Clientes, models.RESTRICT, blank=True, null=True, verbose_name='Cliente')
    numero = models.CharField(max_length=32)
    fecha = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    restante = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.ForeignKey(Tipos_comprobante, models.RESTRICT, blank=True, null=True, verbose_name='Tipo')

    def __str__(self):
        return str(self.numero)
    class Meta:
        db_table = 'comprobantes'
        verbose_name = 'Comprobante'
        verbose_name_plural = 'Comprobantes' 

class Cuotas(models.Model):
    poliza = models.ForeignKey(Polizas, models.RESTRICT, blank=True, null=True, verbose_name='Poliza')
    nro_cuota = models.IntegerField()
    fecha_venc = models.DateField(blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_cancelacion = models.DateField(blank=True, null=True)
    restante = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 'usado por notas de credito (importe negativo) para informar cuanto queda disponible',
    rendicion = models.ForeignKey(Rendiciones, models.RESTRICT, blank=True, null=True, verbose_name='Rendicion')
    nro_comprobante = models.ForeignKey(Comprobantes, models.RESTRICT, blank=True, null=True, verbose_name='Comprobante')
 
    def __str__(self):
        return str(self.nro_cuota)
    class Meta:
        db_table = 'cuotas_polizas'
        verbose_name = 'Cuota'
        verbose_name_plural = 'Cuotas' 
        unique_together = ['poliza_id', 'nro_cuota']

class Pagos(models.Model):
    fecha = models.DateField(blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=2)
    cuota = models.ForeignKey(Cuotas, models.RESTRICT, blank=True, null=True, verbose_name='Cuota')
    comprobante = models.ForeignKey(Comprobantes, models.RESTRICT, blank=True, null=True, verbose_name='Comprobante')
    
    def __str__(self):
        return str(self.importe)
    class Meta:
        db_table = 'pagos_cuotas'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos de cuotas' 


class Cheques (models.Model):
    status = models.BooleanField(default=True, verbose_name='Activo')
    cliente = models.ForeignKey(Clientes, models.RESTRICT, blank=True, null=True, verbose_name='Cliente')
    banco = models.ForeignKey(Banco, models.RESTRICT, blank=True, null=True, verbose_name='Banco')
    sucursal = models.ForeignKey(Bancosucu, models.RESTRICT, blank=True, null=True, verbose_name='Sucursal')
    numero = models.CharField(max_length=32)
    fecha = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    restante = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.numero)
    class Meta:
        db_table = 'cheques'
        verbose_name = 'cheque'
        verbose_name_plural = 'cheques' 