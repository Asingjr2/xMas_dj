from django.urls import path

from . import views
from .views import LogRegView

urlpatterns = [
    path("", views.LogRegView.as_view(), name="log_reg")
]

