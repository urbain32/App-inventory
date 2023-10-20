from django.contrib import admin
from django.urls import path,include
# we can also import the app views and created it url directly in the project urls
from user.views import register,profile
# using the built in login logout of django
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/',register.registerView,name='user-register'),
    path('profile/',profile.profile,name='user-profile'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='user-logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)