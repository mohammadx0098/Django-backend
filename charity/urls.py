from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('charities.urls')),
    path('accounts/', include('accounts.urls')),
    path('about-us/', include('about_us.urls')),
    path(
        "schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"
    ),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
