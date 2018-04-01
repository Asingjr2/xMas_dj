from django.urls import path

from . import views
from .views import HomeView, EnterMembersView, DeleteListView

app_name = "secret_santa"
urlpatterns = [
    path('', HomeView.as_view(), name='santa_home'),
    path('<uuid:pk>/delete', DeleteListView.as_view(), name='delete_list'),
    path('enter_members', EnterMembersView.as_view(), name='enter_members'),

    path('logout/', views.logout_view, name="logout"),
]