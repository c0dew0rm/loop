import csv
from itertools import islice

from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import *


@api_view(['POST'])
def uploadStoresFromCsv(request):
    file = request.FILES['file']

    # let's check if it is a csv file
    if not file.name.endswith('.csv'):
        return HttpResponse(request, 'THIS IS NOT A CSV FILE')

    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)

    objs = []
    store_keys = {}

    for row in reader:
        if store_keys.get(row['store_id']) is None:
            objs.append(Store(store_id=int(row['store_id']), timezone_str=row['timezone_str']))
            store_keys[row['store_id']] = ""

    Store.objects.bulk_create(objs)

    return HttpResponse("Successful.")


@api_view(['POST'])
def uploadBusinessFoursFromCsv(request):
    try:
        file = request.FILES['file']
        # let's check if it is a csv file
        if not file.name.endswith('.csv'):
            return HttpResponse(request, 'THIS IS NOT A CSV FILE')
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

    except Exception as e:
        print("Exception: ", e)
        return HttpResponse("Some exception occoured.")


@api_view(['POST'])
def uploadStatusfromcsv(request):
    try:
        file = request.FILES['file']
        # let's check if it is a csv file
        if not file.name.endswith('.csv'):
            return HttpResponse(request, 'THIS IS NOT A CSV FILE')
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        objs = []
        store_keys = {}
        store_id_list = list(Store.objects.values_list('store_id', flat=True))
        print(store_id_list)

        count= 0
        for row in reader:
            store_id = row['store_id']
            timestamp_utc = row['timestamp_utc']
            status = row['status']
            status_ = False;
            if status == "active":
                status_ = True

            store_key = str(store_id) + "@" + str(timestamp_utc)
            if store_key not in store_keys:
                if store_id not in store_id_list:
                    count = count+1

                    # push data into database

                objs.append(Status(store_id=int(store_id), status = status_, timestamp=timestamp_utc))
                store_keys[store_key] = True
        print(count)
        Status.objects.bulk_create(objs)
        return HttpResponse("Successful.")

    except Exception as e:
        print("Exception: ", e)
        return HttpResponse("Some exception occoured.")
