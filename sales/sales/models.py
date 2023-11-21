from django.db import models
from django.db.models.deletion import DO_NOTHING


class Canal(models.Model):
    nombre = models.CharField(max_length=120)


class Cliente(models.Model):
    ruc = models.CharField(max_length=120)
    nombrefactura = models.CharField(max_length=300)
    nombrefantasia = models.CharField(max_length=300)
    canalobj = models.ForeignKey('Canal', DO_NOTHING)


class Producto(models.Model):
    codigo = models.IntegerField()
    prod_marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)


class Precios(models.Model):
    articuloobj = models.ForeignKey('Producto', DO_NOTHING)
    canalobj = models.ForeignKey('Canal', DO_NOTHING)
    precio = models.FloatField()
    fecha_vigencia = models.DateField()


class Orders(models.Model):
    pedido_numero = models.BigIntegerField(unique=True)
    pdvobj = models.ForeignKey(Cliente, DO_NOTHING)
    doc_tipo = models.CharField(max_length=80)
    doc_fecha = models.DateField()
    doc_numero = models.BigIntegerField(default=0)
    anulado_040 = models.BooleanField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(null=True, max_length=80)


class OrdersDetail(models.Model):
    orderobj = models.ForeignKey(Orders, DO_NOTHING)
    artobj = models.ForeignKey(Producto, DO_NOTHING)
    cantidad_original = models.IntegerField()
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    iva_10 = models.FloatField()
    gravada_10 = models.FloatField()
    iva_5 = models.FloatField()
    gravada_5 = models.FloatField()
    exenta = models.FloatField()
    anulado_040 = models.BooleanField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(null=True, max_length=80)
