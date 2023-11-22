from django.urls import path

from .views import *

app_name = 'application'


urlpatterns = [
   path('application/create', CreateApplicationView.as_view(), name='create'),
   path('application/delete/<int:pk>', DeleteApplication.as_view(), name='delete'),
   path('application/change_status/<int:pk>', ChangeStatusView.as_view(), name='change_status'),

   path('category', IndexCategory.as_view(), name='index_category'),
   path('category/delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),
   path('category/create', CreateCategory.as_view(), name='create_category'),
]
