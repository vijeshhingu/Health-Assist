from django.urls import path
from . import views

app_name = 'diagnosis'  # Define the namespace name
urlpatterns = [
    path('', views.diagnosis, name='diagnosis'),
]
