from django.urls import path
from . import views
urlpatterns = [
    path('backend/api/', views.ListingsCreate.as_view() ),
]