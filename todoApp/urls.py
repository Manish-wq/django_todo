"""
URL configuration for todoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employee/', include('employee.urls')),

    path('get-todo/', views.get_todo, name='get_todo'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('mark-as-done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('update-todo/<int:pk>/', views.update_todo, name='update_todo'),
    # path('delete-todo/<int:pk>/', views.delete_todo, name='delete_todo'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
