# encoding: ISO8859-1
from celery import shared_task
import json
import lzstring
from .tools import jsonconvert
from .models import Orders, OrdersDetail


@shared_task
def save_orders_clients(data):
    decompressed_data = lzstring.LZString().decompressFromBase64(data)
    orders_data = json.loads(decompressed_data, encoding='iso-8859-1', object_hook=jsonconvert)
    for cliente_id, items in orders_data.items():
        for item in items:
            order = Orders(
                pedido_numero=item['pedido_numero'],
                pdvobj_id=cliente_id,
                doc_tipo=item['doc_tipo'],
                doc_fecha=item['doc_fecha'],
                doc_numero=item['doc_numero'],
                anulado_040=item['anulado_040'],
                anulado_040_fecha=item['anulado_040_fecha'],
                anulado_040_por_gecos=item['anulado_040_por_gecos'],
            )
            order.save()

            order_detail = OrdersDetail(
                orderobj=order,
                artobj_id=item['articulo_id'],
                cantidad_original=item['cantidad_original'],
                cantidad=item['cantidad'],
                precio_unitario=item['precio_unitario'],
                iva_10=item['iva_10'],
                gravada_10=item['gravada_10'],
                iva_5=item['iva_5'],
                gravada_5=item['gravada_5'],
                exenta=item['exenta'],
                anulado_040=item['anulado_040'],
                anulado_040_fecha=item['anulado_040_fecha'],
                anulado_040_por_gecos=item['anulado_040_por_gecos'],
            )
            order_detail.save()

    return "Data saved successfully"
