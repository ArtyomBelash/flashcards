from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.urls')),
    path('auth/', include('profiles.urls')),
    path('auth/', include('profiles.urls')),
    path('api/v1/', include('api.urls')),

]
