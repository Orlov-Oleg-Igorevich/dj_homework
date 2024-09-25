from django.urls import path
from measurement import views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', views.TempView.as_view(), name='temp_sensor'),
    path('sensors/<pk>/', views.SensorViewDetails.as_view(), name='temp_pk'),
    path('measurements/', views.SensorViewDetails.as_view(), name='temp'),

]
