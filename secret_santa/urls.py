from django.urls import path

from . import views
from .views import (
    HomeView,
    EnterMembersView,
    DeleteListView,
    DeleteMemberView,
    ListDetailView,
    UpdateMemberView,
    UpdateListView,
    AddMemberView,
    GiftPairsView
)

app_name = "secret_santa"
urlpatterns = [
    # List CRUD
    path('', HomeView.as_view(), name='santa_home'),
    path('<uuid:list_id>/', ListDetailView.as_view(), name='list_detail'),
    path('list/update/<uuid:pk>/', UpdateListView.as_view(), name='update_list'),
    path('list/delete/<uuid:pk>/', DeleteListView.as_view(), name='delete_list'),

    # Secret santa list creation and display
    path('gift_pairs/<uuid:pk>/', GiftPairsView.as_view(), name='gift_pairs'),

    # Member CRUD
    path('enter_members/', EnterMembersView.as_view(), name='enter_members'),
    path('add_member/<uuid:pk>', AddMemberView.as_view(), name='add_member'),
    path('update/<uuid:pk>/', UpdateMemberView.as_view(), name='update_member'),
    path('delete/<uuid:pk>/', DeleteMemberView.as_view(), name='delete_member'),

    path('logout/', views.logout_view, name="logout"),
]