from django.db import models
from django.db.models.deletion import SET_NULL


class Canal(models.Model):
    nombre = models.CharField(max_length=120)


class Cliente(models.Model):
    ruc = models.CharField(max_length=120)
    nombrefactura = models.CharField(max_length=300)
    nombrefantasia = models.CharField(max_length=300)
    canalobj = models.ForeignKey('Canal', SET_NULL)


class Producto(models.Model):
    codigo = models.IntegerField()
    prod_marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)


class Precios(models.Model):
    articuloobj = models.ForeignKey('Producto', SET_NULL)
    canalobj = models.ForeignKey('Canal', SET_NULL)
    precio = models.FloatField()
    fecha_vigencia = models.DateField()


class Orders(models.Model):
    pedido_numero = models.BigIntegerField(unique=True)
    pdvobj = models.ForeignKey(Cliente, SET_NULL)
    doc_tipo = models.CharField(max_length=80)
    doc_fecha = models.DateField()
    doc_numero = models.BigIntegerField(default=0)
    anulado_040 = models.BooleanField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(null=True)


class OrdersDetail(models.Model):
    orderobj = models.ForeignKey(Orders, SET_NULL)
    artobj = models.ForeignKey(Producto, SET_NULL)
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
    anulado_040_por_gecos = models.CharField(null=True)
