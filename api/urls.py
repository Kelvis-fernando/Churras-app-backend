from django.urls import path
from .views import ChurrasView

urlpatterns = [
    path('churras/', ChurrasView.as_view(), name="churras"),
]
