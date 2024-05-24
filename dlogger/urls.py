from django.contrib import admin
from django.urls import path,include 
from django.contrib.auth import views as auth_views 
from users import views as users_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), 
    path('register/', users_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), 
    path('profile/', users_view.profile, name='user-profile'),
    path('p/<int:id>/', users_view.profile_view, name='user-profile-view'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)