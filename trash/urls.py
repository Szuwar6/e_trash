from django.urls import path
from . import views
app_name = 'trash'

urlpatterns = [
    path("trashes-list-view/", views.TrashListView.as_view(), name="trashes-list-view"),
    path("trashes-create-view/", views.TrashCreateView.as_view(), name="trashes-create-view"),
    path("trashes-detail-view/<pk>", views.TrashDetailView.as_view(), name="trashes-detail-view"),
    path("trashes-update-view/<pk>", views.TrashUpdateView.as_view(), name="trashes-update-view"),
    path("trashes-delete-view/<pk>", views.TrashDeleteView.as_view(), name="trashes-delete-view"),
    path("ewastes-list-view/", views.EWasteListView.as_view(), name="ewastes-list-view"),
    path("ewastes-create-view/", views.EWasteCreateView.as_view(), name="ewastes-create-view"),
    path("ewastes-detail-view/<pk>", views.EWasteDetailView.as_view(), name="ewastes-detail-view"),
    path("ewastes-update-view/<pk>", views.EWasteUpdateView.as_view(), name="ewastes-update-view"),
    path("ewastes-delete-view/<pk>", views.EWasteDeleteView.as_view(), name="ewastes-delete-view"),
    path("rwastes-list-view/", views.RWasteListView.as_view(), name="rwastes-list-view"),
    path("rwastes-create-view/", views.RWasteCreateView.as_view(), name="rwastes-create-view"),
    path("rwastes-detail-view/<pk>", views.RWasteDetailView.as_view(), name="rwastes-detail-view"),
    path("rwastes-update-view/<pk>", views.RWasteUpdateView.as_view(), name="rwastes-update-view"),
    path("rwastes-delete-view/<pk>", views.RWasteDeleteView.as_view(), name="rwastes-delete-view"),
    path("hwastes-list-view/", views.HWasteListView.as_view(), name="hwastes-list-view"),
    path("hwastes-create-view/", views.HWasteCreateView.as_view(), name="hwastes-create-view"),
    path("hwastes-detail-view/<pk>", views.HWasteDetailView.as_view(), name="hwastes-detail-view"),
    path("hwastes-update-view/<pk>", views.HWasteUpdateView.as_view(), name="hwastes-update-view"),
    path("hwastes-delete-view/<pk>", views.HWasteDeleteView.as_view(), name="hwastes-delete-view"),
    path("lswastes-list-view/", views.LSWasteListView.as_view(), name="lswastes-list-view"),
    path("lswastes-create-view/", views.LSWasteCreateView.as_view(), name="lswastes-create-view"),
    path("lswastes-detail-view/<pk>", views.LSWasteDetailView.as_view(), name="lswastes-detail-view"),
    path("lswastes-update-view/<pk>", views.LSWasteUpdateView.as_view(), name="lswastes-update-view"),
    path("lswastes-delete-view/<pk>", views.LSWasteDeleteView.as_view(), name="lswastes-delete-view"),
    ]