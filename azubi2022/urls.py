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
    path('schwarz/', quiz.views.schwarz, name='schwarz'),
    path('schwarzfehler1/', quiz.views.schwarzfehler1, name='schwarzfehler1'),
    path('schwarzfehler2/', quiz.views.schwarzfehler2, name='schwarzfehler2'),
    path('schwarzfehler3/', quiz.views.schwarzfehler3, name='schwarzfehler3'),
    path('schwarz2/', quiz.views.schwarz2, name='schwarz2'),
    path('schwarz2fehler1/', quiz.views.schwarz2fehler1, name='schwarz2fehler1'),
    path('schwarz2fehler2/', quiz.views.schwarz2fehler2, name='schwarz2fehler2'),
    path('schwarz2fehler3/', quiz.views.schwarz2fehler3, name='schwarz2fehler3'),
    path('schwarz3/', quiz.views.schwarz3, name='schwarz3'),
    path('schwarz3fehler1/', quiz.views.schwarz3fehler1, name='schwarz3fehler1'),
    path('schwarz3fehler2/', quiz.views.schwarz3fehler2, name='schwarz3fehler2'),
    path('schwarz3fehler3/', quiz.views.schwarz3fehler3, name='schwarz3fehler3'),
    path('schwarz4/', quiz.views.schwarz4, name='schwarz4'),
    path('schwarz4fehler1/', quiz.views.schwarz4fehler1, name='schwarz4fehler1'),
    path('schwarz4fehler2/', quiz.views.schwarz4fehler2, name='schwarz4fehler2'),
    path('schwarz4fehler3/', quiz.views.schwarz4fehler3, name='schwarz4fehler3'),
    path('schwarz5/', quiz.views.schwarz5, name='schwarz5'),
    path('schwarz5fehler1/', quiz.views.schwarz5fehler1, name='schwarz5fehler1'),
    path('schwarz5fehler2/', quiz.views.schwarz5fehler2, name='schwarz5fehler2'),
    path('schwarz5fehler3/', quiz.views.schwarz5fehler3, name='schwarz5fehler3'),
    path('gruen/', quiz.views.gruen, name='gruen'),
    path('gruenfehler1/', quiz.views.gruenfehler1, name='gruenfehler1'),
    path('gruenfehler2/', quiz.views.gruenfehler2, name='gruenfehler2'),
    path('gruenfehler3/', quiz.views.gruenfehler3, name='gruenfehler3'),
    path('gruen2/', quiz.views.gruen2, name='gruen2'),
    path('gruen2fehler1/', quiz.views.gruen2fehler1, name='gruen2fehler1'),
    path('gruen2fehler2/', quiz.views.gruen2fehler2, name='gruen2fehler2'),
    path('gruen2fehler3/', quiz.views.gruen2fehler3, name='gruen2fehler3'),
    path('gruen3/', quiz.views.gruen3, name='gruen3'),
    path('gruen3fehler1/', quiz.views.gruen3fehler1, name='gruen3fehler1'),
    path('gruen3fehler2/', quiz.views.gruen3fehler2, name='gruen3fehler2'),
    path('gruen3fehler3/', quiz.views.gruen3fehler3, name='gruen3fehler3'),
    path('gruen4/', quiz.views.gruen4, name='gruen4'),
    path('gruen4fehler1/', quiz.views.gruen4fehler1, name='gruen4fehler1'),
    path('gruen4fehler2/', quiz.views.gruen4fehler2, name='gruen4fehler2'),
    path('gruen4fehler3/', quiz.views.gruen4fehler3, name='gruen4fehler3'),
    path('rot/', quiz.views.rot, name='rot'),
    path('rotfehler1/', quiz.views.rotfehler1, name='rotfehler1'),
    path('rotfehler2/', quiz.views.rotfehler2, name='rotfehler2'),
    path('rotfehler3/', quiz.views.rotfehler3, name='rotfehler3'),
    path('rot2/', quiz.views.rot2, name='rot2'),
    path('rot2fehler1/', quiz.views.rot2fehler1, name='rot2fehler1'),
    path('rot2fehler2/', quiz.views.rot2fehler2, name='rot2fehler2'),
    path('rot2fehler3/', quiz.views.rot2fehler3, name='rot2fehler3'),
    path('rot3/', quiz.views.rot3, name='rot3'),
    path('rot3fehler1/', quiz.views.rot3fehler1, name='rot3fehler1'),
    path('rot3fehler2/', quiz.views.rot3fehler2, name='rot3fehler2'),
    path('rot3fehler3/', quiz.views.rot3fehler3, name='rot3fehler3'),
    path('rot4/', quiz.views.rot4, name='rot4'),
    path('rot4fehler1/', quiz.views.rot4fehler1, name='rot4fehler1'),
    path('rot4fehler2/', quiz.views.rot4fehler2, name='rot4fehler2'),
    path('rot4fehler3/', quiz.views.rot4fehler3, name='rot4fehler3'),
    path('rotglueck/', quiz.views.rotglueck, name='rotglueck'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
