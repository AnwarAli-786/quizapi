from django.urls import path, include
from rest_framework import routers
from quizapp.views import QuizViewSet

router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('quizzes/active/', QuizViewSet.as_view({'get': 'get_active_quiz'})),
    path('quizzes/<int:pk>/result/', QuizViewSet.as_view({'get': 'get_quiz_result'})),
]
