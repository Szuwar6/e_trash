from django.urls import path

from accounts import views

app_name = "accounts"

urlpatterns = [
    path("register-user/", views.RegisterUser.as_view(), name="register-user"),
    path(
        "register-recycler/", views.RegisterRecycler.as_view(), name="register-recycler"
    ),
]
