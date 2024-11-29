from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('contract/create/', views.ContractCreate.as_view(), name='contract_create'),
]

