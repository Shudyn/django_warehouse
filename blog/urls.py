"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from articles import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.archive),
    path('clients/', views.client),
    path('contracts/', views.contracts),
    path('deliveries/', views.deliveries),
    path('finances/', views.finances),
    path('jobs/', views.jobs),
    path('opjournal/', views.operations),
    path('registry/', views.registry),
    path('valuables/', views.valuables),
    path('workers/', views.worker),
    path('', views.login),
    path('suppliers/', views.suppliers),
    path('logout/', views.logout_view),
    path('edit/<int:client_id>/', views.edit_entry),
    path('update/<int:client_id>', views.update_entry),
    path('contrpaper/<int:contract_id>', views.contrpaper),
    path('noaccess/', views.no_access),
]


