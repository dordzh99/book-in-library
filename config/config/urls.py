from django.contrib import admin
from django.urls import include, path

from users.views import register_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('users/', include('users.urls')),
]
