from django.urls import path

from . import views

urlpatterns = [
    path("csv/upload/stores", views.uploadStoresFromCsv.as_view(), name="uploadStoresCsv"),
    path("csv/upload/businesshours", views.uploadBusinessFoursFromCsv.as_view(), name="uploadBusinessFoursFromCsv"),
    path("csv/upload/status", views.uploadStatusfromcsv.as_view(), name="uploadStatusfromcsv"),
    path("", views.uploadStatusfromcsv.as_view(), name="uploadStatusfromcsv"),
]
