# encoding: ISO8859-1
from celery import shared_task
import redis
import json
import lzstring
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .tools import jsonconvert
from .tasks import save_orders_clients

redis_connection = redis.StrictRedis(host='localhost', port=6379, db=0)


@shared_task
def save_sales_data(gart):
    if type(gart) == dict:
        gart = json.dumps(gart)
    compressed_data = lzstring.LZString().compressToBase64(gart)
    redis_connection.set('sales_data', compressed_data)


@method_decorator(csrf_exempt, name='dispatch')
class SaveSalesDataView(View):
    def post(self, request, *args, **kwargs):
        # data = request.POST  # this is an empty dict! Can't tell why. Using instead request.body
        data = request.body.decode()  # decode it from byte
        save_sales_data.delay(data)
        return JsonResponse({'status': 'success'})


@method_decorator(csrf_exempt, name='dispatch')
class RetrieveDataView(View):
    def get(self, request, *args, **kwargs):
        compressed_data = redis_connection.get('sales_data')
        decoded_data = compressed_data.decode()  # decode it from byte
        decompressed_data = lzstring.LZString().decompressFromBase64(decoded_data)
        data_dict = json.loads(decompressed_data, encoding='iso-8859-1', object_hook=jsonconvert)
        for cus in data_dict["clientes"]:
            save_orders_clients(cus)
        return JsonResponse({'status': 'success', "data": decompressed_data})
