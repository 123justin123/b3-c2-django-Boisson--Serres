from django.contrib import admin
from django.urls import path
from PasswordManager.views import Login, Signup, Dashboard, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/signup/', Signup, name='signup'),
    path('accounts/logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
]
