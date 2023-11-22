from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
   path('accounts/login', BBLoginView.as_view(), name='login'),
   path('accounts/profile/', profile, name='profile'),
   path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
   path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
   path('accounts/register/', RegisterUserView.as_view(), name='register'),
   path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
]
