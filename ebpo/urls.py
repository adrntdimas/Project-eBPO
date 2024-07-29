from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/'),
    path('auth/', include('login_app.urls')),
]