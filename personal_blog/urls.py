from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views as blog_views  # Import blog views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include your blog app's URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', blog_views.signup, name='signup'),  # Reference signup view from blog_views
]
