from celery import shared_task
import json
import lzstring

@shared_task
def save_orders_clients(data):
    # Descomprimir datos con lzstring
    decompressed_data = lzstring.LZString().decompressFromBase64(data)

    # Convertir JSON a tipo de datos Python
    orders_data = json.loads(decompressed_data)

    # Guardar datos en la base de datos
    # Implementa la lógica necesaria para guardar en la base de datos de Django