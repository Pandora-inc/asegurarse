CREATE TABLE IF NOT EXISTS _access_permissions (
 module_id serial NOT NULL PRIMARY KEY,
 user_id numeric(10) NOT NULL
);
CREATE INDEX IF NOT EXISTS FK__permisos_acceso_usuarios ON _access_permissions(user_id);
COMMENT ON TABLE "_access_permissions" IS 'solo para accesos específicos';
COMMENT ON COLUMN _access_permissions.user_id IS 'usuario autorizado';

CREATE TABLE IF NOT EXISTS _concurrency_semaph (
 module_id numeric(11) NOT NULL,
 record_id numeric(11) NOT NULL,
 action_id numeric(11) NOT NULL,
 user_id numeric(11) NOT NULL
) ;
COMMENT ON COLUMN _concurrency_semaph.action_id IS 'action in progress';
COMMENT ON COLUMN _concurrency_semaph.user_id IS 'user performing action in progress';

CREATE TABLE IF NOT EXISTS _modules (
 id numeric(10) NOT NULL PRIMARY KEY,
 name varchar(45) NOT NULL
) ;

CREATE TABLE IF NOT EXISTS _security_auth (
 module_id numeric(11) NOT NULL,
 user_id numeric(11) NOT NULL,
 p_open smallint DEFAULT '0',
 p_read smallint DEFAULT NULL,
 p_add smallint DEFAULT '0',
 p_edit smallint DEFAULT '0',
 p_prnumeric smallint DEFAULT NULL
);
COMMENT ON TABLE _security_auth IS 'only for needed user auth';
COMMENT ON COLUMN _security_auth.p_open IS 'permission to open a module';
COMMENT ON COLUMN _security_auth.p_read IS 'permission to read records';

CREATE TABLE IF NOT EXISTS _session_events (
 session_id numeric(11) NOT NULL,
 level numeric(11) NOT NULL,
 action_id numeric(11) NOT NULL,
 module_id numeric(11) NOT NULL,
 record_id numeric(11) NOT NULL,
 timestamp timestamp NOT NULL
) ;
COMMENT ON COLUMN _session_events.session_id IS 'session has the user_id';
COMMENT ON COLUMN _session_events.level IS 'session stack counter';
COMMENT ON COLUMN _session_events.action_id IS 'hardcoded in app';


CREATE TABLE IF NOT EXISTS _sessions (
 id numeric(10) NOT NULL PRIMARY KEY,
 user_id numeric(10) NOT NULL,
 start timestamp NOT NULL,
 watchdog timestamp DEFAULT NULL
) ;
COMMENT ON COLUMN _sessions.id IS 'no autoincremental';

CREATE TABLE IF NOT EXISTS _taskman (
 session_id numeric(10) NOT NULL PRIMARY KEY,
 task_id numeric(10) NOT NULL,
 reference numeric(10) NOT NULL
) ;
COMMENT ON COLUMN _taskman.reference IS 'id of record or module';

CREATE TABLE IF NOT EXISTS _tasks (
 id serial NOT NULL PRIMARY KEY,
 descrip varchar(45) NOT NULL
) ;

CREATE TABLE IF NOT EXISTS _users (
 id serial NOT NULL PRIMARY KEY,
 status numeric(10) NOT NULL,
 name varchar(45) NOT NULL,
 password varchar(32) DEFAULT NULL
) ;

CREATE TABLE IF NOT EXISTS auth_group (
 id serial NOT NULL PRIMARY KEY,
 name varchar(150) UNIQUE NOT NULL
) ;

CREATE TABLE IF NOT EXISTS django_content_type (
 id serial NOT NULL PRIMARY KEY,
 app_label varchar(100) NOT NULL,
 model varchar(100) NOT NULL,
 UNIQUE (app_label,model)
) ;


CREATE TABLE IF NOT EXISTS auth_permission (
 id serial NOT NULL PRIMARY KEY,
 name varchar(255) NOT NULL,
 content_type_id integer NOT NULL,
 codename varchar(100) NOT NULL,
 UNIQUE (content_type_id,codename),
 CONSTRAINT const_auth_permission_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type (id)
) ;

CREATE TABLE IF NOT EXISTS auth_group_permissions (
 id serial NOT NULL PRIMARY KEY,
 group_id integer NOT NULL,
 permission_id integer NOT NULL,
 UNIQUE (group_id,permission_id),
 CONSTRAINT const_auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission (id),
 CONSTRAINT const_auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group (id)
) ;
CREATE INDEX IF NOT EXISTS auth_group_permissio_permission_id_index ON auth_group_permissions(permission_id);



CREATE TABLE IF NOT EXISTS auth_user (
 id serial NOT NULL PRIMARY KEY,
 password varchar(128) NOT NULL,
 last_login timestamp (6) DEFAULT NULL,
 is_superuser smallint NOT NULL,
 username varchar(150) NOT NULL,
 first_name varchar(150) NOT NULL,
 last_name varchar(150) NOT NULL,
 email varchar(254) NOT NULL,
 is_staff smallint NOT NULL,
 is_active smallint NOT NULL,
 date_joined timestamp (6) NOT NULL,
 UNIQUE (username)
) ;


CREATE TABLE IF NOT EXISTS auth_user_groups (
 id serial NOT NULL PRIMARY KEY,
 user_id integer NOT NULL,
 group_id integer NOT NULL,
 UNIQUE (user_id,group_id),
 CONSTRAINT const_auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group (id),
 CONSTRAINT const_auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;
CREATE INDEX IF NOT EXISTS auth_user_groups_group_id_index ON auth_user_groups(group_id);

CREATE TABLE IF NOT EXISTS auth_user_user_permissions (
 id serial NOT NULL PRIMARY KEY,
 user_id integer NOT NULL,
 permission_id integer NOT NULL,
 UNIQUE (user_id,permission_id),
 CONSTRAINT const_auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission (id),
 CONSTRAINT const_auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;
CREATE INDEX IF NOT EXISTS auth_user_user_permi_permission_id_index ON auth_user_user_permissions(permission_id);

CREATE TABLE IF NOT EXISTS banco (
 id serial NOT NULL PRIMARY KEY,
 descrip varchar(32) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS bancosucu (
 id serial NOT NULL PRIMARY KEY,
 descrip varchar(32) DEFAULT NULL,
 codigo varchar(16) DEFAULT NULL,
 banco_id integer NOT NULL,
 CONSTRAINT const_bancosucu_ibfk_1 FOREIGN KEY (banco_id) REFERENCES banco (id) ON UPDATE CASCADE
) ;
CREATE INDEX IF NOT EXISTS id_banco ON bancosucu(banco_id);


CREATE TABLE IF NOT EXISTS cheques (
 id serial NOT NULL PRIMARY KEY,
 status smallint DEFAULT NULL,
 cliente_id numeric(11) DEFAULT NULL,
 banco_id numeric(11) DEFAULT NULL,
 sucursal_id numeric(11) DEFAULT NULL,
 numero varchar(32) DEFAULT NULL,
 fecha date DEFAULT NULL,
 fecha_ingreso date DEFAULT NULL,
 valor decimal(10,2) DEFAULT NULL,
 restante decimal(10,2) DEFAULT NULL,
 observaciones varchar(96) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS clientes (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL DEFAULT '1',
 nombre varchar(64) NOT NULL,
 descrip varchar(256) DEFAULT NULL,
 direccion varchar(62) DEFAULT NULL,
 postal_id numeric(11) DEFAULT NULL,
 telefonos varchar(32) DEFAULT NULL,
 email varchar(62) DEFAULT NULL,
 establecim varchar(64) DEFAULT NULL,
 actividad varchar(62) DEFAULT NULL,
 nacimiento date DEFAULT NULL,
 tipodoc_id numeric(11) DEFAULT NULL,
 documento varchar(11) DEFAULT NULL,
 cuit varchar(13) DEFAULT NULL,
 fecha date DEFAULT NULL,
 seg_retiro smallint DEFAULT NULL,
 corresp smallint DEFAULT NULL,
 reg_num varchar(16) DEFAULT NULL,
 reg_categ varchar(16) DEFAULT NULL,
 reg_juris varchar(16) DEFAULT NULL,
 reg_venc date DEFAULT NULL,
 productor_id numeric(11) DEFAULT NULL,
 banco varchar(62) DEFAULT NULL,
 banco_suc varchar(8) DEFAULT NULL,
 banco_caja varchar(16) DEFAULT NULL,
 banco_ctacte varchar(16) DEFAULT NULL,
 debaut smallint DEFAULT NULL,
 observaciones text 
) ;
COMMENT ON COLUMN clientes.corresp IS 'Correspondencia';



CREATE TABLE IF NOT EXISTS clientes_mediosdepago (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL,
 cliente_id numeric(11) NOT NULL,
 mediodepago_id numeric(11) NOT NULL,
 numero varchar(64) DEFAULT NULL
) ;
CREATE INDEX IF NOT EXISTS idx1 ON clientes_mediosdepago(cliente_id,mediodepago_id);


CREATE TABLE IF NOT EXISTS coberturas (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL DEFAULT '1',
 nombre varchar(64)  NOT NULL,
 seccion_id numeric(11) NOT NULL
) ;

CREATE TABLE IF NOT EXISTS codigo_productor (
 id serial NOT NULL PRIMARY KEY,
 productor_id numeric(11) DEFAULT NULL,
 compania_id numeric(11) DEFAULT NULL,
 codigo varchar(20) DEFAULT NULL
) ;

CREATE TABLE IF NOT EXISTS companias (
 id serial NOT NULL PRIMARY KEY,
 status smallint NOT NULL DEFAULT '1',
 nombre varchar(32) NOT NULL,
 razon_social varchar(64) DEFAULT NULL,
 direccion varchar(32) DEFAULT NULL,
 telefonos varchar(32) DEFAULT NULL,
 cuit varchar(13) DEFAULT NULL,
 productor_id numeric(11) DEFAULT NULL,
 comis_con_iva smallint DEFAULT NULL,
 ib_comis_prod smallint DEFAULT NULL,
 ib_comis_cobr smallint DEFAULT NULL,
 comis_cobranzas smallint DEFAULT NULL,
 dias_primer_cuota numeric(11) DEFAULT NULL,
 liquidaciones decimal(10,0) DEFAULT NULL,
 primer_cuota_iva smallint DEFAULT NULL,
 prop_iva smallint DEFAULT NULL,
 agente_iva smallint DEFAULT NULL,
 fecha_firma_convenio date DEFAULT NULL,
 observaciones text 
) ;
COMMENT ON COLUMN companias.ib_comis_prod IS 'Ing.Brutos sobre comisiones Productor';
COMMENT ON COLUMN companias.ib_comis_cobr IS 'Ing.Brutos sobre comisiones Cobrador';
COMMENT ON COLUMN companias.comis_cobranzas IS 'Comision de cobranzas';
COMMENT ON COLUMN companias.primer_cuota_iva IS 'Primer cuota todo el IVA';
COMMENT ON COLUMN companias.prop_iva IS 'Proporciona IVA en la primer cuota';
COMMENT ON COLUMN companias.agente_iva IS 'Agente de retencion de IVA';


CREATE TABLE IF NOT EXISTS comprobantes (
 id serial NOT NULL PRIMARY KEY,
 cliente_id numeric(11) DEFAULT NULL,
 numero varchar(32) DEFAULT NULL,
 fecha date DEFAULT NULL,
 valor decimal(10,2) DEFAULT NULL,
 restante decimal(10,2) DEFAULT NULL,
 tipo numeric(11) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS cuotas_polizas (
 id serial NOT NULL PRIMARY KEY,
 poliza_id numeric(11) NOT NULL,
 nro_cuota numeric(11) DEFAULT NULL,
 fecha_venc date DEFAULT NULL,
 importe decimal(10,2) DEFAULT NULL,
 saldo decimal(10,2) DEFAULT NULL,
 fecha_cancelacion date DEFAULT NULL,
 restante decimal(10,2) DEFAULT NULL,
 rendicion_id numeric(11) DEFAULT NULL,
 nro_comprobante varchar(8) DEFAULT NULL
) ;
CREATE INDEX IF NOT EXISTS poliza_idx ON cuotas_polizas(poliza_id);
COMMENT ON COLUMN cuotas_polizas.restante IS 'usado por notas de credito (importe negativo) para informar cuanto queda disponible';



CREATE TABLE IF NOT EXISTS django_admin_log (
 id serial NOT NULL PRIMARY KEY,
 action_time timestamp (6) NOT NULL,
 object_id text ,
 object_repr varchar(200) NOT NULL,
 action_flag smallint NOT NULL,
 change_message text NOT NULL,
 content_type_id integer DEFAULT NULL,
 user_id integer NOT NULL,
 CONSTRAINT const_django_admin_log_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type (id),
 CONSTRAINT const_django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;
CREATE INDEX IF NOT EXISTS index_django_admin_log_content_type ON django_admin_log(content_type_id);
CREATE INDEX IF NOT EXISTS index_django_admin_log_content_type_id ON django_admin_log(content_type_id);


CREATE TABLE IF NOT EXISTS django_migrations (
 id serial NOT NULL PRIMARY KEY,
 app varchar(255) NOT NULL,
 name varchar(255) NOT NULL,
 applied timestamp (6) NOT NULL 
) ;


CREATE TABLE IF NOT EXISTS django_session (
 session_key varchar(40) PRIMARY KEY NOT NULL,
 session_data text NOT NULL,
 expire_date timestamp(6) NOT NULL
) ;
CREATE INDEX IF NOT EXISTS django_session_expire_date ON django_session(expire_date);


CREATE TABLE IF NOT EXISTS mediosdepago (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL,
 nombre varchar(64) NOT NULL,
 tipo varchar(16) NOT NULL
) ;
COMMENT ON TABLE mediosdepago IS 'Medios de Pago';


CREATE TABLE IF NOT EXISTS monedas (
 id serial NOT NULL PRIMARY KEY,
 status smallint NOT NULL,
 nombre varchar(45) DEFAULT NULL,
 simbolo varchar(5) DEFAULT NULL,
 cambio decimal(10,2) DEFAULT NULL
);


CREATE TABLE IF NOT EXISTS operaciones (
 id serial NOT NULL PRIMARY KEY,
 ord_num varchar(32) NOT NULL,
 ord_fecha date NOT NULL,
 pol_num varchar(32) DEFAULT NULL,
 pol_fecha date DEFAULT NULL,
 pol_fecha_recep date DEFAULT NULL,
 vigencia_desde date DEFAULT NULL,
 vigencia_hasta date DEFAULT NULL,
 bien_asegurado varchar(80) DEFAULT NULL,
 direccion varchar(32) DEFAULT NULL,
 postal_id numeric(11) DEFAULT NULL,
 telefonos varchar(32) DEFAULT NULL,
 email varchar(32) DEFAULT NULL,
 provincia_id numeric(11) DEFAULT NULL,
 cliente_id numeric(11) DEFAULT NULL,
 productor_id numeric(11) DEFAULT NULL,
 organizador_id numeric(11) DEFAULT NULL,
 compania_id numeric(11) DEFAULT NULL,
 seccion_id numeric(11) DEFAULT NULL,
 cobertura_id numeric(11) DEFAULT NULL,
 moneda_id numeric(11) DEFAULT NULL,
 tipopoliza_id numeric(11) DEFAULT NULL,
 tiposoli_id numeric(11) DEFAULT NULL,
 mediodepago_id numeric(11) DEFAULT NULL,
 nro_mediopago varchar(32) DEFAULT NULL,
 suma decimal(10,0) DEFAULT NULL,
 prima decimal(10,0) DEFAULT NULL,
 premio decimal(10,0) DEFAULT NULL,
 recargos decimal(10,0) DEFAULT NULL,
 bonificacion decimal(10,0) DEFAULT NULL,
 iva decimal(10,0) DEFAULT NULL,
 ing_brutos decimal(10,0) DEFAULT NULL,
 produccion decimal(10,0) DEFAULT NULL,
 cobranza decimal(10,0) DEFAULT NULL,
 recup_gastos decimal(10,0) DEFAULT NULL,
 restante decimal(10,0) DEFAULT NULL,
 cant_cuotas numeric(11) DEFAULT NULL,
 nota_credito smallint DEFAULT NULL,
 riesgo_desc text,
 siniestro01 varchar(100) DEFAULT NULL,
 siniestro02 varchar(100) DEFAULT NULL,
 siniestro03 varchar(100) DEFAULT NULL,
 siniestro04 varchar(100) DEFAULT NULL
) ;
CREATE INDEX IF NOT EXISTS idx_ord_num ON operaciones(ord_num);
CREATE INDEX IF NOT EXISTS idx_pol_num ON operaciones(pol_num);




CREATE TABLE IF NOT EXISTS polizas (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL,
 numero varchar(62) DEFAULT NULL,
 orden_id numeric(11) DEFAULT NULL,
 fecha date DEFAULT NULL,
 fecha_recepcion date DEFAULT NULL,
 vigencia_desde date DEFAULT NULL,
 vigencia_hasta date DEFAULT NULL,
 num_poliza varchar(20) DEFAULT NULL,
 cliente_id numeric(11) DEFAULT NULL,
 productor_id numeric(11) DEFAULT NULL,
 organizador_id numeric(11) DEFAULT NULL,
 moneda_id numeric(11) DEFAULT NULL,
 compania_id numeric(11) DEFAULT NULL,
 seccion_id numeric(11) DEFAULT NULL,
 cobertura_id numeric(11) DEFAULT NULL,
 suma decimal(11,2) DEFAULT NULL,
 prima decimal(11,2) DEFAULT NULL,
 recargos decimal(11,2) DEFAULT NULL,
 bonificacion decimal(11,2) DEFAULT NULL,
 premio decimal(11,2) DEFAULT NULL,
 iva decimal(10,2) DEFAULT NULL,
 ing_brutos decimal(10,2) DEFAULT NULL,
 tipopoliza_id smallint DEFAULT NULL,
 riesgo_desc text,
 riesgo_valor decimal(11,2) DEFAULT NULL,
 bien_asegurado varchar(80) DEFAULT NULL,
 produccion decimal(11,2) DEFAULT NULL,
 cobranza decimal(11,2) DEFAULT NULL,
 recup_gastos decimal(11,2) DEFAULT NULL,
 mediodepago_id numeric(11) DEFAULT NULL,
 nro_mediopago varchar(62) DEFAULT NULL,
 direccion varchar(62) DEFAULT NULL,
 postal_id numeric(11) DEFAULT NULL,
 telefonos varchar(62) DEFAULT NULL,
 email varchar(62) DEFAULT NULL,
 provincia_id numeric(11) DEFAULT NULL,
 cant_cuotas numeric(10) DEFAULT NULL,
 siniestro01 varchar(100) DEFAULT NULL,
 siniestro02 varchar(100) DEFAULT NULL,
 siniestro03 varchar(100) DEFAULT NULL,
 siniestro04 varchar(100) DEFAULT NULL,
 nota_credito smallint DEFAULT NULL,
 restante decimal(11,2) DEFAULT NULL 
) ;











CREATE TABLE IF NOT EXISTS ordenes (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL,
 numero numeric(11) DEFAULT NULL,
 fecha date DEFAULT NULL,
 vigencia_desde date DEFAULT NULL,
 vigencia_hasta date DEFAULT NULL,
 cliente_id numeric(11) DEFAULT NULL,
 productor_id numeric(11) DEFAULT NULL,
 organizador_id numeric(11) DEFAULT NULL,
 moneda_id numeric(11) DEFAULT NULL,
 compania_id numeric(11) DEFAULT NULL,
 seccion_id numeric(11) DEFAULT NULL,
 cobertura_id numeric(11) DEFAULT NULL,
 tiposoli_id smallint DEFAULT NULL,
 suma decimal(11,2) DEFAULT NULL,
 prima decimal(11,2) DEFAULT NULL,
 recargos decimal(11,2) DEFAULT NULL,
 bonificacion decimal(11,2) DEFAULT NULL,
 premio decimal(11,2) DEFAULT NULL,
 tipopoliza_id smallint DEFAULT NULL,
 riesgo_desc text,
 riesgo_valor decimal(11,2) DEFAULT NULL,
 bien_asegurado varchar(80) DEFAULT NULL,
 produccion decimal(11,2) DEFAULT NULL,
 cobranza decimal(11,2) DEFAULT NULL,
 recup_gastos decimal(11,2) DEFAULT NULL,
 mediodepago_id numeric(11) DEFAULT NULL,
 nro_mediopago varchar(32) DEFAULT NULL,
 responsable varchar(30) DEFAULT NULL,
 direccion varchar(32) DEFAULT NULL,
 postal_id numeric(11) DEFAULT NULL,
 poliza_id integer DEFAULT NULL,
 num_poliza_ref varchar(32) DEFAULT NULL,
 cod_productor varchar(16) DEFAULT NULL,
 flag varchar(1) DEFAULT NULL,
 codigo_productor numeric(11) DEFAULT NULL,
 orden_productor numeric(11) DEFAULT NULL,
 UNIQUE (numero,flag),
 CONSTRAINT const_FK_ORDENES_POLIZAS FOREIGN KEY (poliza_id) REFERENCES polizas (id)
) ;
CREATE INDEX IF NOT EXISTS poliza_id ON ordenes(poliza_id);

CREATE TABLE IF NOT EXISTS organizadores (
 id serial NOT NULL PRIMARY KEY,
 status numeric(11) NOT NULL DEFAULT '1',
 nombre varchar(32) NOT NULL,
 direccion varchar(64) DEFAULT NULL,
 telefonos varchar(64) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS pagos_cuotas (
 id serial NOT NULL PRIMARY KEY,
 fecha date NOT NULL,
 importe decimal(10,2) NOT NULL,
 tipo varchar(2) DEFAULT NULL,
 cuota_id numeric(11) DEFAULT NULL,
 comprobante_id numeric(11) DEFAULT NULL 
) ;

















CREATE TABLE IF NOT EXISTS polizas_rendicion (
 id serial NOT NULL PRIMARY KEY,
 rendicion_id numeric(11) NOT NULL DEFAULT '0',
 poliza_id numeric(11) NOT NULL DEFAULT '0',
 cuota_id numeric(11) NOT NULL DEFAULT '0',
 PRIMARY KEY (id,rendicion_id,poliza_id,cuota_id)
) ;

CREATE TABLE IF NOT EXISTS postal (
 id serial NOT NULL PRIMARY KEY,
 status smallint NOT NULL DEFAULT '1',
 cp varchar(4) NOT NULL,
 cpa varchar(16) NOT NULL,
 referencia varchar(64) NOT NULL,
 provincia_id integer DEFAULT NULL,
 CONSTRAINT const_postal_ibfk_1 FOREIGN KEY (provincia_id) REFERENCES provincias (id)
) ;
CREATE INDEX IF NOT EXISTS idx_provincia_id ON postal(provincia_id);

CREATE TABLE IF NOT EXISTS productores (
 id serial NOT NULL PRIMARY KEY,
 nombre varchar(32) NOT NULL,
 status smallint NOT NULL DEFAULT '1',
 direccion varchar(64) DEFAULT NULL,
 telefonos varchar(64) DEFAULT NULL,
 postal_id numeric(11) DEFAULT NULL,
 email varchar(32) DEFAULT NULL,
 org1_id numeric(11) DEFAULT NULL,
 org2_id numeric(11) DEFAULT NULL,
 matricula varchar(10) DEFAULT NULL,
 ultima_orden numeric(11) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS provincias (
 id serial NOT NULL PRIMARY KEY,
 nombre varchar(32) NOT NULL,
 orden numeric(11) NOT NULL,
 status smallint NOT NULL 
) ;
COMMENT ON COLUMN provincias.orden IS 'orden de aparicion';

CREATE TABLE IF NOT EXISTS rendiciones (
 id serial NOT NULL PRIMARY KEY,
 status smallint DEFAULT NULL,
 fecha date DEFAULT NULL,
 productor_id numeric(11) DEFAULT NULL,
 fecha_cierre date DEFAULT NULL,
 total decimal(10,2) DEFAULT NULL,
 compania_id numeric(11) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS secciones (
 id serial NOT NULL PRIMARY KEY,
 nombre varchar(32) NOT NULL,
 descrip varchar(64) DEFAULT NULL,
 status numeric(11) NOT NULL DEFAULT '1',
 abrev varchar(10) DEFAULT NULL 
);

CREATE TABLE IF NOT EXISTS tipos_comprobante (
 id serial NOT NULL PRIMARY KEY,
 descrip varchar(16) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS tiposdoc (
 id serial NOT NULL PRIMARY KEY,
 status smallint DEFAULT NULL,
 nombre varchar(5) DEFAULT NULL,
 descrip varchar(32) DEFAULT NULL 
) ;

CREATE TABLE IF NOT EXISTS tipospedido (
 id serial NOT NULL PRIMARY KEY,
 nombre varchar(32) NOT NULL,
 status smallint NOT NULL DEFAULT '1' 
) ;

CREATE TABLE IF NOT EXISTS tipospoliza (
 id serial NOT NULL PRIMARY KEY,
 nombre varchar(32) NOT NULL,
 status smallint NOT NULL DEFAULT '1' 
) ;
