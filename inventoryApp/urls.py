from django.contrib import admin
from django.urls import path,include
# we can also import the app views and created it url directly in the project urls
from user.views import register,profile
# using the built in login logout of django
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/',register.registerView,name='user-register'),
    path('profile/',profile.profile,name='user-profile'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='user-logout')
]
