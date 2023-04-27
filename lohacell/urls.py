"""lohacell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.apps import apps
from front import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    path('admin/', admin.site.urls),
    path('lohacell/', include(apps.get_app_config('oscar').urls[0])),
    path('', views.index, name='index'),
    path('detox_capsule/', views.detox_capsule, name='detox_capsule'),
    path('detox_mimi/', views.detox_mimi, name='detox_mimi'),
    path('policy_personal/', views.policy_personal, name='policy_personal'),
    path('policy_agree/', views.policy_agree, name='policy_agree'),
    path('introduce/', views.introduce, name='introduce'),
    path('lohacell_system/', views.lohacell_system, name='lohacell_system'),
    path('research/', views.research, name='research'),
    path('medicine/', views.medicine, name='medicine'),
    path('notice/', views.notice, name='notice'),
    path('payment_20230427114723/', views.payment, name='payment'),
    path('basicprocessor_20230427114723/', views.basicprocessor, name='basicprocessor'),
    
]
