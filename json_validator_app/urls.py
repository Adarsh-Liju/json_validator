"""
URL configuration for json_validator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import (
    EpochConverter, MainScreen,
    ValidateJSON, PrettifyJSON
)

urlpatterns = [
    path("", MainScreen.as_view(), name="main_screen"),
    path("validate-json/", ValidateJSON.as_view(), name="validate_json"),
    path("pretty-json/", PrettifyJSON.as_view(), name="prettify_json"),
    path("epoch-converter/", EpochConverter.as_view(), name="epoch_converter")
]
