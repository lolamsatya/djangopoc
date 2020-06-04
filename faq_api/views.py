from rest_framework import viewsets

from .serializers import FrequentlyAskedQuestionsSerializer
from .models import FrequentlyAskedQuestions


class FrequentlyAskedQuestionsViewSet(viewsets.ModelViewSet):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer