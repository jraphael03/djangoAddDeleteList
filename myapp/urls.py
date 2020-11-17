from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('person', views.person),
    path('persons', views.persons),
    path('updateperson', views.updateperson),
    path('updateperson/<id>', views.updateperson),
    path('deleteperson/<id>', views.deleteperson),
    path('getTotal', views.getTotal),
]

