from django.urls import path
from .views import home, contacto, reportes

urlpatterns = [
    path('', home,name="home"),
    path('contacto/', contacto,name="contacto"),
    path('reportes/', reportes,name="reportes"),
]
