"""personal_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from homepage import views
from django.urls import path


urlpatterns = [

    path("business/", views.business_page, name="business_page"),
    path("personal/", views.private_page, name="personal_page"),
    path("skills/", views.skills_page, name="skills_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("impressum/", views.impressum_page, name="impressum_page")
]
