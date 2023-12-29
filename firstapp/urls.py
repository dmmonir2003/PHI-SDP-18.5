from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='homepage'),
    path('signup/', views.user_signup,name='user_signup'),
    path('login/', views.user_login,name='user_login'),
    path('user_logout/', views.user_logout,name='user_logout'),
    path('pass_change/', views.pass_change,name='pass_change'),
    path('pass_change2/', views.pass_change2,name='pass_change2'),
    path('profile/', views.profile,name='profile'),
    
]
