"""e_trash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from e_trash.views import HomepageView, HomepageClientView, HomepageRecyclerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("trash/", include("trash.urls")),
    path("base/", include("base.urls")),
    path("", HomepageView.as_view(), name="homepage"),
    path("homepage-client/", HomepageClientView.as_view(), name="homepage-client"),
    path(
        "homepage-recycler/", HomepageRecyclerView.as_view(), name="homepage-recycler"
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
]
