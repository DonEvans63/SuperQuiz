from django.urls import path

from .views import QuestionDetailView
from . import views

# app_name = "super_quiz_app"

urlpatterns = [
    path("", views.home, name="home"),
    # path("super_quiz_app", IndexView.as_view, name="index"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path('login/', views.login, name="login"),
]
