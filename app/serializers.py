#======================== REST FRAMEWORK IMPORTS ========================#
from rest_framework import serializers

#============================= APP IMPORTS ==============================#
from app.models import Score, Answer#, Statement


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'


# class StatementSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Statement
# 		fields = ['statement',]


class ScoreSerializer(serializers.ModelSerializer):
	answer_set = AnswerSerializer(many=True)
	# statement = StatementSerializer()

	class Meta:
		model = Score
		fields = '__all__'

	def create(self, validated_data):
		answers_data = validated_data.pop('answer_set')
		# statement_data = validated_data.pop('statement')
		score = validated_data.pop("score")
		nickname = validated_data.pop("nickname")
		statement = validated_data.pop("statement")
		score = Score.objects.create(score=score, nickname=nickname, statement=statement)

		for answer_data in answers_data:
			# print("ANSWER_DATA: ")
			# print(answer_data.get("answer"))
			Answer.objects.create(answer=answer_data.get("answer"))

		return score
