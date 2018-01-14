#============================ Django IMPORTS ==============================#
from django.contrib.auth.models import User

#======================== REST FRAMEWORK IMPORTS ========================#
from rest_framework import serializers
from rest_framework.authtoken.models import Token

#============================= APP IMPORTS ==============================#
from app.models import Score

class ScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Score
		fields = '__all__'
