from django.contrib import admin
from django.urls import path
from SSApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='Home'),
    path('signup',views.signup,name='Signup'),
    path('loginuser',views.loginuser,name='login'),
    path('logoutuser',views.logoutuser,name='logout'),
    path('udash',views.udash,name='User Dashboard'),
    path('recscreen',views.recscreen,name='Record Screen'),
    path('vid/',views.vid,name='Video Playback'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
