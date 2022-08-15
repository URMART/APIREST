
from django.urls import path
from api.views import CompanieView

name='api'
urlpatterns = [
    path('companies/', CompanieView.as_view(),name='companies_list'),
    path('companies/<int:id>', CompanieView.as_view(),name='companies_Process'), #as_view se utiliza para comvertir una clase a una vista
    
]
