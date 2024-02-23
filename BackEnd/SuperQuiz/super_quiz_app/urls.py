from django.urls import path

from .views import QuestionDetailView

# app_name = "super_quiz_app"

urlpatterns = [
    # path("super_quiz_app", IndexView.as_view, name="index"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
]