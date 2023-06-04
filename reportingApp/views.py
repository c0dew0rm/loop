import csv
from itertools import islice

from django.http import HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

class uploadStoresFromCsv(APIView):
    
    def post(self, request):
        file = request.FILES['file']
        # let's check if it is a csv file
        if not file.name.endswith('.csv'):
            return HttpResponse(request, 'THIS IS NOT A CSV FILE')

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        objs = []
        for row in reader:
            objs.append(Store(store_id= int(row['store_id']), timezone_str=row['timezone_str']))

        Store.objects.bulk_create(objs)

        return Response("Successful.")

class uploadBusinessFoursFromCsv(APIView):

    def post(self, request):
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
    



class uploadStatusfromcsv(APIView):
    def post(self, request):
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
