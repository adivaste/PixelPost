from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.user_signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('profile', views.profile, name='profile'),
    # path('profile/<str:username>', views.profile, name='userprofile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
