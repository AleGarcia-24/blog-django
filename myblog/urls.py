from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculadoras/', include('calculadoras.urls')),
    path('', include('blog.urls')),
]