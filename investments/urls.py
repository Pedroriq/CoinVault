from django.urls import path
from investments.views import create_investment, list_investment, update_investment, delete_investment

urlpatterns = [
    path('', list_investment, name='list_investment'),
    path('create/', create_investment, name='create_investment'),
    path('update/<int:pk>/', update_investment, name='update_investment'),
    path('delete/<int:pk>/', delete_investment, name='delete_investment'),
]