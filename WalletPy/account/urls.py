from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="profile"),
    path('update/', views.update, name="profile_update"),
    path('i18n/', include('django.conf.urls.i18n')),
]