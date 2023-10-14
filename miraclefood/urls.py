"""
URL configuration for miraclefood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from accounts.views import (
    login_view,
    logout_view,
    register_view,
    check_username,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('dishes/', include('dishes.urls')),
    path('ingredients/', include('ingredients.urls')),
    path('recipes/', include('recipes.urls')),
    path('menus/', include('menus.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('stock/', include('stock.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),


]


htmx_url_patterns=[
    path('check_username/', check_username, name='check-username'),

]
urlpatterns+=htmx_url_patterns