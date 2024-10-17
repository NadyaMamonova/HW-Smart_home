from django.urls import path

from measurement.views import SensorView, SensorViewUpdate, MeasurementView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensor/<pk>/', SensorViewUpdate.as_view()),
    path('measurement/', MeasurementView.as_view()),
]
