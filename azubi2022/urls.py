"""azubi2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import quiz.views

urlpatterns = [
    path('', quiz.views.home, name='home'),
    path('red/', quiz.views.red, name='red'),
    path('red2/<str:antwort>', quiz.views.red2, name='red2'),
    path('red3/', quiz.views.red3, name='red3'),
    path('red3/<str:liste>/<str:antwort>', quiz.views.red3, name='red3'),
    path('red4/', quiz.views.red4, name='red4'),
    path('red4/<str:liste>/<str:antwort>', quiz.views.red4, name='red4'),
    path('summary/<str:liste>/<str:antwort>', quiz.views.summary, name='summary'),
    path('green/', quiz.views.green, name='green'),
    path('green2/<str:antwort>', quiz.views.green2, name='green2'),
    path('green3/', quiz.views.green3, name='green3'),
    path('green3/<str:liste>/<str:antwort>', quiz.views.green3, name='green3'),
    path('green4/', quiz.views.green4, name='green4'),
    path('green4/<str:liste>/<str:antwort>', quiz.views.green4, name='green4'),
    path('summary2/<str:liste>/<str:antwort>', quiz.views.summary2, name='summary2'),
    path('black/', quiz.views.black, name='black'),
    path('black2/<str:antwort>', quiz.views.black2, name='black2'),
    path('black3/', quiz.views.black3, name='black3'),
    path('black3/<str:liste>/<str:antwort>', quiz.views.black3, name='black3'),
    path('black4/', quiz.views.black4, name='black4'),
    path('black4/<str:liste>/<str:antwort>', quiz.views.black4, name='black4'),
    path('black5/', quiz.views.black5, name='black5'),
    path('black5/<str:liste>/<str:antwort>', quiz.views.black5, name='black5'),
    path('summary3/<str:liste>/<str:antwort>', quiz.views.summary3, name='summary3'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
