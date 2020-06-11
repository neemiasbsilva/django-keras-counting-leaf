from django.urls import path
from .views import *


urlpatterns = [
    path('', RegressionListView.as_view(), name='list'),
    path('create/', RegressionCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RegressionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RegressionDeleteView.as_view(), name='delete'),
]