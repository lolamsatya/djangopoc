from django.db import models


class FrequentlyAskedQuestions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    shaid = models.CharField(max_length = 512, primary_key = True)

    def __str__(self):
        return self.question

