from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.CreateMailingAPIView.as_view(), name='create_mailing'),
    path('list/', views.ListMailingAPIView.as_view(), name='list_mailing')
]
