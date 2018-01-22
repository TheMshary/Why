from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app.serializers import ScoreSerializer
from app.models import Score, Answer
import json

# Create your views here.
class ReactAppView(APIView):

	def get(self, request):
		return render(request, 'index.html', {})


class LeaderboardView(APIView):

	permission_classes = (AllowAny,)

	def get(self, request):
		leaderboard = Score.objects.all().order_by('-score')
		data = {
			"top": ScoreSerializer(leaderboard, many=True).data
		}
		print("LEADERBOARD: ")
		for score in data.get('top'):
			print(score)
		return Response(data, status=status.HTTP_200_OK)

	def post(self, request):
		print("REQUEST.DATA: ")
		print(request.data)
		score = request.data.get("score")
		statement = request.data.get("statement")
		answers = json.loads(request.data.get("answer_set"))
		print("ANSWERS: ")
		print(answers)
		i = 0
		while i < len(answers):
			answers[i].pop('id', None)
			i = i + 1
		nickname = request.data.get("nickname")
		if nickname == "":
			nickname = "Anonymous"

		data = {
			"nickname": nickname,
			"score": score,
			"statement": statement,
			"answer_set": answers
		}
		serializer = ScoreSerializer(data=data)
		if serializer.is_valid():
			score_obj = serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			print(serializer.errors)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlagView(APIView):

	permission_classes = (AllowAny,)

	def post(self, request):
		answer_id = request.data.get("answer_id")
		answer = Answer.objects.get(id=answer_id)
		answer.flags += 1
		answer.save()
		return Response(status=status.HTTP_200_OK)