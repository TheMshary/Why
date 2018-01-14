from django.db import models

# Create your models here.
class Score(models.Model):
	score = models.PositiveIntegerField(default=0)
	nickname = models.CharField(max_length=50, default="Anonymous")
	statement = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return "%s\t\t%s" % (self.score, self.nickname)


class Answer(models.Model):
	answer = models.CharField(max_length=100)
	score = models.ForeignKey(Score, on_delete=models.CASCADE, null=True)
	flags = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.answer
