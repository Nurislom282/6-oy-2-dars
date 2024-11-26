"""
URL configuration for homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import home,page2,page3,page4,page5,page6,page7,page8,page9,page10

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('page2/', page2),
    path('page3/', page3),
    path('page4/', page4),
    path('page5/', page5),
    path('page6/', page6),
    path('page7/', page7),
    path('page8/', page8),
    path('page9/', page9),
    path('page10/', page10),
]
