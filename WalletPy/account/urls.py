from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="profile"),
    path('update/', views.update, name="profile_update"),
]