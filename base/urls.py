from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path(
        "clients-list-view/", views.ClientListView.as_view(), name="clients-list-view"
    ),
    path(
        "clients-detail-view/",
        views.ClientDetailView.as_view(),
        name="clients-detail-view",
    ),
    path(
        "clients-update-view/",
        views.ClientUpdateView.as_view(),
        name="clients-update-view",
    ),
    path(
        "clients-delete-view/<pk>",
        views.ClientDeleteView.as_view(),
        name="clients-delete-view",
    ),
    # path("clients-form-view/", views.client_address_create, name = "clients-form-view"),
    path(
        "clients-form-view/",
        views.ClientAddressCreateView.as_view(),
        name="clients-form-view",
    ),
    path(
        "recyclers-form-view/",
        views.RecyclerFormView.as_view(),
        name="recyclers-form-view",
    ),
    # path("orders-user-view/", views.order_user, name = "orders-user-view"),
    path("orders-user-view/", views.OrderCreateView.as_view(), name="orders-user-view"),
    path(
        "orders-detail-view/<pk>",
        views.OrderDetailView.as_view(),
        name="orders-detail-view",
    ),
    path(
        "address-detail-view/",
        views.AddressDetailView.as_view(),
        name="address-detail-view",
    ),
    path(
        "address-update-view/",
        views.AddressUpdateView.as_view(),
        name="address-update-view",
    ),
    path(
        "recycler-detail-view/",
        views.RecyclerDetailView.as_view(),
        name="recycler-detail-view",
    ),
    path(
        "recycler-update-view/",
        views.RecyclerUpdateView.as_view(),
        name="recycler-update-view",
    ),
    path(
        "orders-delete-view/<pk>",
        views.OrderDeleteView.as_view(),
        name="orders-delete-view",
    ),
    path(
        "orders-recycler-detail-view/<pk>",
        views.OrderRecyclerDetailView.as_view(),
        name="orders-recycler-detail-view",
    ),
    path(
        "orders-client-list/",
        views.OrdersClientList.as_view(),
        name="orders-client-list",
    ),
    path(
        "orders-recycler-list/",
        views.OrdersRecyclerList.as_view(),
        name="orders-recycler-list",
    ),
    path("check-recycler/", views.CheckRecycler.as_view(), name="check-recycler"),
    path("check-profile/", views.CheckProfile.as_view(), name="check-profile"),
]
