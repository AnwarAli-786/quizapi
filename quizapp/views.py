from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import Quiz
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def list(self, request):
        queryset = Quiz.objects.all()
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Quiz.objects.all()
        quiz = get_object_or_404(queryset, pk=pk)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    def get_active_quiz(self, request):
        queryset = Quiz.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now(), status='active')
        if queryset.exists():
            quiz = queryset.first()
            serializer = QuizSerializer(quiz)
            return Response(serializer.data)
        else:
            return Response({'error': 'No active quiz found.'})

    def get_quiz_result(self, request, pk=None):
        quiz = Quiz.objects.get(pk=pk)
        if quiz.status != 'finished':
            return Response({'error': 'Quiz is not yet finished.'})
        else:
            return Response({'right_answer': quiz.right_answer})

