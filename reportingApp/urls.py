from django.urls import path

from . import views

urlpatterns = [
    path("csv/upload/stores", views.uploadStoresFromCsv, name="uploadStoresCsv"),
    path("csv/upload/businesshours", views.uploadBusinessFoursFromCsv, name="uploadBusinessFoursFromCsv"),
    path("csv/upload/status", views.uploadStatusfromcsv, name="uploadStatusfromcsv"),
    path("", views.uploadStatusfromcsv, name="uploadStatusfromcsv"),
]
