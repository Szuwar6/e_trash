from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path("clients-list-view/", views.ClientListView.as_view(), name="clients-list-view"),
    path("clients-detail-view/<pk>", views.ClientDetailView.as_view(), name="clients-detail-view"),
    path("clients-update-view/<pk>", views.ClientUpdateView.as_view(), name="clients-update-view"),
    path("clients-delete-view/<pk>", views.ClientDeleteView.as_view(), name="clients-delete-view"),
    path("clients-form-view/", views.client_address_create, name = "clients-form-view"),
    path("recyclers-form-view/", views.RecyclerFormView.as_view(), name = "recyclers-form-view"),
    path("orders-form-view/", views.OrderFormView.as_view(), name = "orders-form-view"),
    ]