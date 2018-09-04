from rest_framework import serializers
from .models import profesional, language, language_tips
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = language
		fields = ('url', 'name')
class LanguageTipsSerializer(serializers.HyperlinkedModelSerializer):
	language_id = LanguageSerializer(read_only=True)
	class Meta:
		model = language_tips
		fields = ('url','title','description','language_id')
class ProfesionalSerializer(serializers.HyperlinkedModelSerializer):
	languages = LanguageSerializer(read_only=True,many=True)
	class Meta:
		model = profesional
		fields = ('url', 'firstname','lastname','languages')
	@transaction.atomic
	def update(self, instance, validated_data):
		profesional_id   = instance.__dict__.get("id")
		profesion_member = profesional.objects.get(pk=profesional_id)

		languages = self.initial_data.get("languages")
		profesion_member.languages.clear()
		for lang in languages:
			try:
				profesion_member.languages.add( language.objects.get(pk=lang) )
			except:
				pass

		instance.__dict__.update(**validated_data)
		instance.save()
		return instance