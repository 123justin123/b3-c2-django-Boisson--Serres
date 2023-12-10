from django.contrib import admin
from django.urls import path
from PasswordManager.views import Login, Signup, Dashboard, Logout, edit_site, delete_site

urlpatterns = [
    path('', Login.as_view(), name='root'),
    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/signup/', Signup, name='signup'),
    path('accounts/logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('edit-site/<int:site_id>/', edit_site, name='edit_site'),
    path('delete-site/<int:site_id>/', delete_site, name='delete_site'),
]
