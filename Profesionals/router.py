from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from .serializers import UserSerializer, ProfesionalSerializer, LanguageSerializer, LanguageTipsSerializer
from .viewsets import UserViewSet, ProfesionalViewSet, LanguageViewSet, LanguageTipsViewSet


router = routers.DefaultRouter()
router.register( r'users', UserViewSet )
router.register( r'profesionals', ProfesionalViewSet )
router.register( r'language', LanguageViewSet )
router.register( r'language_tips', LanguageTipsViewSet )