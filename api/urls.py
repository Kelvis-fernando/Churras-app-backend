from django.urls import path
from .views import ChurrasView, ChurrasDetail

urlpatterns = [
    path('churras/', ChurrasView.as_view(), name="churras"),
    path('churras/<int:pk>/', ChurrasDetail.as_view(), name="churras_detail"),
]
