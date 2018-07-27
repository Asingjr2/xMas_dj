from django.urls import path
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('secret_santa/', include("secret_santa.urls", namespace= "secret_santa")),
    path('', include("log_reg.urls")),
]
