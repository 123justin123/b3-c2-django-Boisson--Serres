from django.contrib import admin
from django.urls import path
from PasswordManager.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
]
