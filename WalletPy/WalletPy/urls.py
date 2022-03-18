"""WalletPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from portefeuille import views as portefeuille
from market import views as market
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

import custom_auth.views


urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('admin/', admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('portefeuille/', portefeuille.index, name="wallet"),
    path('fav/<int:id>/',views.favorite_add, name="favorite_add"),
    path('marche/', market.index, name="market"),
    path('register/', custom_auth.views.register_request, name="register"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True),name="login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('password_change/', auth_views.PasswordChangeView.as_view(),name="password_change"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_comfirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('profile/', include('account.urls')),
]

handler404 = 'WalletPy.views.error_404'
