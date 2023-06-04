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
    batch_size = 1000
    for row in reader:
        print(type(row['store_id']))
        print(type(row['timezone_str']))
        objs.append(Store(store_id= int(row['store_id']), timezone_str=row['timezone_str']))

    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Store.objects.bulk_create(batch, batch_size)

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

    except Exception as e:
        print("Exception: ", e)
        return HttpResponse("Some exception occoured.")
