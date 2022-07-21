from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path("clients-list-view/", views.ClientListView.as_view(), name="clients-list-view"),
    path("clients-detail-view/", views.ClientDetailView.as_view(), name="clients-detail-view"),
    path("clients-update-view/", views.ClientUpdateView.as_view(), name="clients-update-view"),
    path("clients-delete-view/<pk>", views.ClientDeleteView.as_view(), name="clients-delete-view"),
    path("clients-form-view/", views.client_address_create, name = "clients-form-view"),
    path("recyclers-form-view/", views.RecyclerFormView.as_view(), name = "recyclers-form-view"),
    path("orders-form-view/", views.OrderFormView.as_view(), name = "orders-form-view"),
    path("orders-user-view/", views.order_user, name = "orders-user-view"),
    path("orders-list/", views.orders_list, name="orders-list"),
    path("orders-detail-view/<pk>", views.OrderDetailView.as_view(), name="orders-detail-view"),
    path("address-detail-view/", views.AddressDetailView.as_view(), name="address-detail-view"),
    path("address-update-view/", views.AddressUpdateView.as_view(), name="address-update-view"),
    path("recycler-detail-view/", views.RecyclerDetailView.as_view(), name="recycler-detail-view"),
    path("recycler-update-view/", views.RecyclerUpdateView.as_view(), name="recycler-update-view"),
    path("orders-delete-view/<pk>", views.OrderDeleteView.as_view(), name="orders-delete-view"),
    path("orders-recycler-list/", views.orders_recycler_list, name="orders-recycler-list"),
    path("orders-recycler-detail-view/<pk>", views.OrderRecyclerDetailView.as_view(), name="orders-recycler-detail-view"),
    ]