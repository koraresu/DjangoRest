from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import profesional, language, language_tips
from .serializers import UserSerializer, ProfesionalSerializer, LanguageSerializer, LanguageTipsSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
	queryset         = User.objects.all()
	serializer_class = UserSerializer
class ProfesionalViewSet(viewsets.ModelViewSet):
	queryset         = profesional.objects.all()
	serializer_class = ProfesionalSerializer
class LanguageViewSet(viewsets.ModelViewSet):
	queryset         = language.objects.all()
	serializer_class = LanguageSerializer
class LanguageTipsViewSet(viewsets.ModelViewSet):
	queryset         = language_tips.objects.all()
	serializer_class = LanguageTipsSerializer