from django.urls import path

from .views import *

app_name = 'application'

urlpatterns = [
   path('application/create', CreateApplicationView.as_view(), name='create'),
   path('application/delete/<int:pk>', DeleteApplication.as_view(), name='delete')
]
