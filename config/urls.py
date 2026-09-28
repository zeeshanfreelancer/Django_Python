
from django.contrib import admin
from django.urls import include, path
from users.views import hello

urlpatterns = [
    path('', hello, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
