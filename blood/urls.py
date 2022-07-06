


from . import views
from django.urls import path



urlpatterns = [
    path('api/stock/', views.StockList.as_view()),
    path('api/bloodrequest/', views.BloodRequestList.as_view()),
]



